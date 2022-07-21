import imageio
import numpy as np
from PIL import Image
import milestone1


def readImage(path):
    try:
        return imageio.imread(path)
    except:
        return "File tidak ditemukan."

image = readImage("../test/1_1_Before.jpg")
new_image = np.array(milestone1.negative(image))
img = Image.fromarray(new_image,'RGB')
img.save('../test/1_1_After.jpg')