import os
from PIL import Image

def main():
    folder = input("Enter folder location: ")

    files = os.listdir(folder)
    for file in files:
        if(file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")):
            print(file)
            create_thumbnail(folder, file)
        else:
            print("File extension not supported")

# Create thumbnail
def create_thumbnail(folder, file):
    if(dir_exists(folder) == False):
        create_dir(folder)
    image = Image.open(folder + "/" + file)
    image.thumbnail((128, 128))
    image.save(folder + "/thumbnails/" + file)

def create_dir(folder):
    os.makedirs(folder + "/thumbnails")

def dir_exists(folder):
    if not os.path.exists(folder + "/thumbnails"):
        return False
    else:
        return True

if __name__ == "__main__":
    main()