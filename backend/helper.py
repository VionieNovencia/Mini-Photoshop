import imageio
import numpy as np

def readImage(path):
    try:
        return imageio.imread(path)
    except:
        return "File tidak ditemukan."

def new_filename(filename, increment):
    if "." in filename:
        extension = filename.split(".")[1]
        filename = filename.split(".")[0]
        filename = filename.split("_")
        name = len(filename)
        try:
            addition = int(filename[name-1]) + int(increment)
        except:
            if increment == "base":
                addition = 0
            else:
                addition = increment
        filename = filename[:name-1]
        filename = "_".join(filename)
        return filename + "_" + str(addition) + "." + extension

def get_filename (filename, addition):
    extension = filename.split(".")[1]
    filename = filename.split(".")[0]
    return filename + "_" + addition + "." + extension

def copy_image(src, dest):
    image = readImage(src)
    image = np.asarray(image)
    imageio.imwrite(dest, image)
    return dest
