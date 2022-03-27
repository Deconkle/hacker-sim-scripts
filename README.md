# hacker-sim-scripts

#### What are these?

These are scripts I've made for the game "Hacker Simulator", sold on [Steam](https://store.steampowered.com/app/1754840/Hacker_Simulator/) and developed by Save All Studios.

These scripts are not ran ingame, these are external scripts that aid in, or automate gameplay. I will assume readers are already familiar with game mechanics, if you are not you may find [this steam guide](https://steamcommunity.com/sharedfiles/filedetails/?id=2645422003) helpful.

# hackersim_auto_phish.py + interests.py
#### What does this do?

These two scripts work together to read phishing target interests from their _fishbook_ profile, then parse them and return which type of account you need to purchase and use in order for your phishing attack to work. 
The game designers wanted you to do this by eye, counting your targets interests, deciding the category of each interest in your head, then choosing the correct account type. *I have goldfish memory, I won't be doing that.* These scripts do the work for me.

#### How does it work?
The easiest method I could come up with to parse target interests using python is to take a windows screenshot ( WIN + SHIFT + S ) and draw the box around their interests. Python grabs the image from your clipboard automatically, it sharpens the image so Google's **Tesseract** OCR module can reliably convert the text in image to a string. Finally, we parse those strings and compare them against a master list of all possible interests.

#### Examples
After starting the script, once you're ingame you'll be able to take a screenshot of ***just*** the targets interest (as shown in red below), and within 4 seconds the python script will print the account type you need to use for a successful phish. 
![20220324083101_1_fishbook_crop](https://user-images.githubusercontent.com/24526230/160257747-3cf6f54c-554e-4de1-8e99-daaced3c19c8.jpg)

## Installation

Install [Python 3.x](https://www.python.org/downloads/) if you don't have it already.

Download python files from this repository

Install Google's [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract#installing-tesseract) and [add it to PATH](https://docs.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14))

Using [Pythons Package Installer (PIP)](https://pip.pypa.io/en/stable/getting-started/), install Pillow (aka PIL) and pytesseract

``pip install Pillow``

``pip install pytesseract`` 

## Usage
I prefer to run the script in a terminal/cmd window. I do this by executing ``py path/to/hackersim_auto_phish.py``. It will help to have this running on another monitor, or otherwise visible along with Hacker Simulator.

### NOTICE
Probably due to my graphics driver weirdness, or possibly the game engine, personally I find trying to take screenshots via the method described above a pain in the ass when the game is in fullscreen. There is no option ingame to change out of fullscreen, so I force it by using the windows keybind ALT+ENTER ingame. Now that it should be in borderless windowed mode, you can choose to make it fullscreen-borderless-windowed by changing to your desired resolution in Graphics options.
