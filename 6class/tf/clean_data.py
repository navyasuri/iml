import re
import cv2
import os
import glob


base = os.environ['HOME']

# Clean Data
for file in glob.glob(base + "/PetsHandsOnExcercise/breeds/*"):
    if not file.endswith(".jpg"):
        #Not ending in .jpg
        print("Deleting (.mat): " + file)
        os.remove(os.path.join(os.getcwd(), file))
    else: 
        flags = cv2.IMREAD_COLOR
        im = cv2.imread(file, flags)
        
        if im is None:
            #Can't read in image
            print("Deleting (None): " + file)
            os.remove(os.path.join(os.getcwd(), file))
            continue
        elif len(im.shape) != 3:
            #Wrong amount of channels
            print("Deleting (len != 3): " + file)
            os.remove(os.path.join(os.getcwd(), file))
            continue
        elif im.shape[2] != 3:
            #Wrong amount of channels
            print("Deleting (shape[2] != 3): " + file)
            os.remove(os.path.join(os.getcwd(), file))
            continue
        with open(os.path.join(os.getcwd(), file), 'rb') as f:
            check_chars = f.read()[-2:]
        if check_chars != b'\xff\xd9':
            #Wrong ending metadata for jpg standard
            print('Deleting (xd9): ' + file)
            os.remove(os.path.join(os.getcwd(), file))
            continue
        if file == "beagle_116.jpg" or file == "chihuahua_121.jpg":
            #Using EXIF Data to determine this
            print('Deleting (corrupt jpeg data): ', file)
            os.remove(os.path.join(os.getcwd(), file))

print('Clean Done.')
