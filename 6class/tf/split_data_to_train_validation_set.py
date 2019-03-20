import os
import re
import errno
import math

# Get breed name from the filename of the image. Imgaes are named "<breedname>_<number>.jpg"
def get_category(file):
    m = re.search("\d", file, re.IGNORECASE)
    if m:
        return file[:m.start() - 1].lower()

# Create directories for the specified path
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

# Goto the directory breeds where data is copied
os.chdir("breeds/")

# Create a sorted list of all the breed names             
file_names = os.listdir("./")
category_names = [ get_category(file) for file in file_names]
category_names = [ name for name in category_names if name is not None ]
category_names = sorted(list(set(category_names)))

# Create directories for all the breeds inside train and validation directories 
for category in category_names:
    make_sure_path_exists("train/" + str(category))
    make_sure_path_exists("val/" + str(category))

# split the data in such a way that 80% goes to train and the rest goes to validation directory
train_ratio = .8
train_txt = {}
test_txt = {}

# Split the data for each category to 80:20 splits
for idx, category in enumerate(category_names):
    category_list = []
    for file in file_names:
        if category.lower() in file.lower():
            category_list.append(file)
    
    category_list = sorted(category_list)
    split_ratio = int(math.floor(len(category_list) * train_ratio))
    train_list = category_list[:split_ratio]
    test_list = category_list[split_ratio:]
    
    # Move the train images to train directory
    for file in train_list:
        os.rename(file, "train/" + str(category) + "/" + file)
        train_txt[str(category) + "/" + file] = idx
        
    # Move the validation images to validation directory.
    for file in test_list:
        os.rename(file, "val/" + str(category) + "/" + file)        
        test_txt[str(category) + "/" + file] = idx

print("Done splitting data")        
        
# Write the breeds names to the file categories.txt
categories = open("categories.txt", "w")
for val in category_names:
    categories.write("{0}\n".format(val))
categories.close()
print("Wrote categories.txt")

print("")
print("Done.")

