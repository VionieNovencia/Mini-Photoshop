from distutils.log import error
from inspect import getfile
import imageio

def readImage(path):
    try:
        return imageio.imread(path)
    except:
        return "File tidak ditemukan."

def new_filename(filename):
    extension = filename.split(".")[1]
    filename = filename.split(".")[0]
    filename = filename.split("_")
    name = len(filename)
    try:
        addition = int(filename[name-1]) + 1
    except:
        return error
    filename = filename[:name-1]
    filename = "_".join(filename)
    return filename + "_" + str(addition) + "." + extension

def get_filename (filename, addition):
    extension = filename.split(".")[1]
    filename = filename.split(".")[0]
    return filename + "_" + addition + "." + extension