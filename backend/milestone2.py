#https://www.geeksforgeeks.org/python-intensity-transformation-operations-on-images/

import numpy as np
from PIL import Image

def brightening(image):
    w,h = image.shape[:2]
    new_image = image
    for i in range(w):
        for j in range(h):
            r,g,b = image[i][j]
            r = r+50
            g = g+50
            b = b+50
            if r<0:
                r = 0
            if g<0:
                g = 0
            if b<0:
                b = 0
            if r>255:
                r = 255
            if g>255:
                g = 255
            if b>255:
                b = 255
            new_image[i][j] = (r,g,b)
    return new_image

def contrast_helper(pix,r1,r2):
    s1 = 0
    s2 = 255
    if (0 <= pix and pix <= r1):
        return (s1 / r1)*pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2

def contrast(image):
    new_image = image
    r1 = np.min(image)
    r2 = np.max(image)
    for i in range(len(image)):
        for j in range(len(image[i])):
            r,g,b = image[i][j]
            r = (r-r1)*(255/(r2-r1))
            g = (g-r1)*(255/(r2-r1))
            b = (b-r1)*(255/(r2-r1))
            new_image[i][j] = (r,g,b)
    return new_image

def logTransformation(image):
    new_image = image
    m = np.max(image)
    c = 255/(np.log(1+m))
    for i in range(len(image)):
        for j in range(len(image[i])):
            r,g,b = image[i][j]
            r = round(c*np.log(1+r))
            g = round(c*np.log(1+g))
            b = round(c*np.log(1+b))
            new_image[i][j] = (r,g,b)
    return new_image

def powerTransformation(image, gamma):
    new_image = image
    for i in range(len(image)):
        for j in range(len(image[i])):
            r,g,b = image[i][j]
            r = round(255*(r/255)**gamma)
            g = round(255*(g/255)**gamma)
            b = round(255*(b/255)**gamma)
            new_image[i][j] = (r,g,b)
    return new_image

image = Image.open("../test/1_1_Before.jpg")
image = np.asarray(image)
new_image = np.array(powerTransformation(image,0.1))
img = Image.fromarray(new_image)
img.save('../test/1_1_After.jpg')