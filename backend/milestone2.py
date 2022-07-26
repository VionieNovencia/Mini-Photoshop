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

def contrast(image):
    new_image = image
    Imin = np.min(image)
    Imax = np.max(image)
    rmin = image[:,:,0].min()
    rmax = image[:,:,0].max()
    gmin = image[:,:,1].min()
    gmax = image[:,:,1].max()
    bmin = image[:,:,2].min()
    bmax = image[:,:,2].max()
    for i in range(len(image)):
        for j in range(len(image[i])):
            r,g,b = image[i][j]
            if Imin == 0 and Imax == 255:
                r = 255*(r-rmin)/(rmax-rmin)
                g = 255*(g-gmin)/(gmax-gmin)
                b = 255*(b-bmin)/(bmax-bmin)
            else:
                r = (r-rmin)*((Imax - Imin)/(rmax - rmin)) + Imin
                g = (g-gmin)*((Imax - Imin)/(gmax - gmin)) + Imin
                b = (b-bmin)*((Imax - Imin)/(bmax - bmin)) + Imin
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

# image = Image.open("../test/1_2_After.jpg")
# image = np.asarray(image)
# # print(image)
# # print('-----------------')
# new_image = np.array(contrast(image))
# # print(new_image)
# img = Image.fromarray(new_image)
# img.save('../test/1_2_After.png')