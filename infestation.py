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

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


def open(i):
    img = cv2.imread("test.jpg", cv2.IMREAD_ANYCOLOR)
    cv2.imshow("I SEE YOU" + str(i), img)
    cv2.waitKey(1000)
    cv2.moveWindow("I SEE YOU"+ str(i), random.randint(0, screen_width),random.randint(0, screen_height));
    t = Timer(2.0, open)
    t.start()
    cv2.destroyAllWindows() # destroy all windows


i = 0 
while i < 15:
    open(i)
    i += 1



