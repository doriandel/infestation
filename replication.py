
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
