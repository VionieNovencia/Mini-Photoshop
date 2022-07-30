import imageio
import numpy as np
from PIL import Image
from milestone1 import *
from milestone2 import *


def readImage(path):
    try:
        return Image.open(path)
    except:
        return "File tidak ditemukan."

image = readImage("../frontend/static/1_2_Before_0.jpg")
image = np.asarray(image)
new_image = np.array(flip_vertical(image))
img = Image.fromarray(new_image,'RGB')
img.save('../frontend/static/1_1_After.jpg')