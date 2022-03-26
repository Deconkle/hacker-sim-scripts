from PIL import ImageGrab, Image, PngImagePlugin, ImageFilter
from time import sleep
import pytesseract
import interests
clipboard = None

def image_handler(image):
    sharpened = image.filter(ImageFilter.SHARPEN)
    out = [line for line in pytesseract.image_to_string(sharpened).split("\n") if len(line) > 1]
    interests.get_working_account_type(out)

def images_are_same(im1, im2):
    if not type(im1) == type(im2):
        return False
    else:
        if type(im1) == PngImagePlugin.PngImageFile and type(im2) == PngImagePlugin.PngImageFile:
            if list(im1.getdata()) == list(im2.getdata()):
                return True
    return False

while True:
    clip = ImageGrab.grabclipboard() # grab our clipboard
    if type(clip) == PngImagePlugin.PngImageFile:
        if not images_are_same(clip, clipboard):
            clipboard = clip # update our global var
            image_handler(clip)
    sleep(4)
