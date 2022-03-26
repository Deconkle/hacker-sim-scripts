from PIL import ImageGrab, Image, PngImagePlugin, ImageFilter
from time import sleep
import pytesseract # OCR, get TEXT(str) from PIL.ImageGrab obj.
import interests # import our additional script. Contains a dict of account_type: [interests], as well as functions to read and count interests, then print

# pip install pillow | install PIL
# pip install pytesseract | install pytesseract, instilation may differ. If it doesn't work ensure pytesseract scripts are in path.

clipboard = None  # global clipboard var. This simply saves what's on our clipboard (ONLY if it's of type PngImageFile!)

def image_handler(image):
    sharpened = image.filter(ImageFilter.SHARPEN) # sharpen image, this has yet to fail me 
    out = [line for line in pytesseract.image_to_string(sharpened).split("\n") if len(line) > 1] # We run OCR here. We loop through the result, split it by backslash, then add it to this new list only if it's NOT and end character added by tesseract.
    interests.get_working_account_type(out)

def images_are_same(im1, im2): # we can't just ask if two Image types are the same:
    if not type(im1) == type(im2):
        return False
    else:
        if type(im1) == PngImagePlugin.PngImageFile and type(im2) == PngImagePlugin.PngImageFile:
            if list(im1.getdata()) == list(im2.getdata()): # we have to check if their data is the same.
                return True
    return False

while True: 
    clip = ImageGrab.grabclipboard() # grab our clipboard
    if type(clip) == PngImagePlugin.PngImageFile: # is our clipboard a png image?
        if not images_are_same(clip, clipboard):  # if the image we just grabbed from clipboard is still saved to our global clipboard var, it doesn't need to be processed again.
            clipboard = clip # update our global var
            image_handler(clip)
    sleep(4) # Sleep for 4 seconds before checking our clipboard again. Can probably be reduced without adverse effects. YMMV
