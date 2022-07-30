#https://www.geeksforgeeks.org/python-intensity-transformation-operations-on-images/

import numpy as np
from PIL import Image

def brightening(image):
    w,h,d = image.shape[:3]
    new_image = np.zeros((w,h,d), np.uint8)

    if d == 4:
        for i in range(len(image)):
            for j in range(len(image[i])):
                r,g,b,a = image[i][j]
                new_image[i][j] = (r+50,g+50,b+50,a)
    elif d == 3:
        for i in range(len(image)):
            for j in range(len(image[i])):
                r,g,b = image[i][j]
                new_image[i][j] = (r+50,g+50,b+50)
    else:
        for i in range(w):
            for j in range(h):
                new_image[i][j] = image[i][j] + 50
    return new_image

def contrast(image):
    w,h,d = image.shape[:3]
    new_image = np.zeros((w,h,d), np.uint8)
    Imin = np.min(image)
    Imax = np.max(image)
    if d == 4 or d == 3:
        rmin = image[:,:,0].min()
        rmax = image[:,:,0].max()
        gmin = image[:,:,1].min()
        gmax = image[:,:,1].max()
        bmin = image[:,:,2].min()
        bmax = image[:,:,2].max()
        if d == 4:
            for i in range(len(image)):
                for j in range(len(image[i])):
                    r,g,b,a = image[i][j]
                    if Imin == 0 and Imax == 255:
                        r = 255*(r-rmin)/(rmax-rmin)
                        g = 255*(g-gmin)/(gmax-gmin)
                        b = 255*(b-bmin)/(bmax-bmin)
                    else:
                        r = (r-rmin)*((Imax - Imin)/(rmax - rmin)) + Imin
                        g = (g-gmin)*((Imax - Imin)/(gmax - gmin)) + Imin
                        b = (b-bmin)*((Imax - Imin)/(bmax - bmin)) + Imin
                    new_image[i][j] = (r,g,b,a)
        else:
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
    else:
        for i in range(len(image)):
            for j in range(len(image[i])):
                new_image[i][j] = (image[i][j]*(255/(Imax-Imin)) + Imin)
    return new_image

def logTransformation(image):
    w,h,d = image.shape[:3]
    new_image = np.zeros((w,h,d), np.uint8)
    m = np.max(image)
    c = 255/(np.log(1+m))
    if d == 4:
        for i in range(len(image)):
            for j in range(len(image[i])):
                r,g,b,a = image[i][j]
                r = round(c*np.log(1+r))
                g = round(c*np.log(1+g))
                b = round(c*np.log(1+b))
                new_image[i][j] = (r,g,b,a)
    elif d == 3:
        for i in range(len(image)):
            for j in range(len(image[i])):
                r,g,b = image[i][j]
                r = round(c*np.log(1+r))
                g = round(c*np.log(1+g))
                b = round(c*np.log(1+b))
                new_image[i][j] = (r,g,b)
    else:
        for i in range(len(image)):
            for j in range(len(image[i])):
                new_image[i][j] = round(c*np.log(1+image[i][j]))
    return new_image

def powerTransformation(image):
    w,h,d = image.shape[:3]
    new_image = np.zeros((w,h,d), np.uint8)
    gamma = 2
    
    if d == 4:
        for i in range(len(image)):
            for j in range(len(image[i])):
                r,g,b,a = image[i][j]
                r = round(255*(r/255)**gamma)
                g = round(255*(g/255)**gamma)
                b = round(255*(b/255)**gamma)
                new_image[i][j] = (r,g,b,a)
    elif d == 3:
        for i in range(len(image)):
            for j in range(len(image[i])):
                r,g,b = image[i][j]
                r = round(255*(r/255)**gamma)
                g = round(255*(g/255)**gamma)
                b = round(255*(b/255)**gamma)
                new_image[i][j] = (r,g,b)
    else:
        for i in range(len(image)):
            for j in range(len(image[i])):
                new_image[i][j] = round(255*(image[i][j]/255)**gamma)
    return new_image