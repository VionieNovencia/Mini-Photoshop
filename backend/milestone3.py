#https://www.pixelstech.net/article/1353768112-Gaussian-Blur-Algorithm
import numpy as np
from PIL import Image

def gaussianblur(image):
    radius = 2
    kernel_size = radius*2+1
    kernel = np.zeros((kernel_size, kernel_size))
    for i in range(-1*radius,radius):
        for j in range(-1*radius,radius):
            kernel[i][j] = round(1/(2*np.pi*1.5*1.5) * np.exp(-1*(i*i+j*j)/(2*1.5*1.5)),3)
    
    sum = 0
    for item in kernel:
        for item2 in item:
            sum += item2

    for i in range (kernel_size):
        for j in range (kernel_size):
            kernel[i][j] = kernel[i][j]/sum

    new_image = image
    w,h = image.shape[:2]
    for i in range(w):
        for j in range(h):
            r = 0
            g = 0
            b = 0
            for k in range(kernel_size):
                for l in range(kernel_size):
                    if i-k >= 0 and i-k < w and j-l >= 0 and j-l < h:
                        r += image[i-k][j-l][0] * kernel[k][l]
                        g += image[i-k][j-l][1] * kernel[k][l]
                        b += image[i-k][j-l][2] * kernel[k][l]
            new_image[i][j] = (r,g,b)
    return new_image

def gaussianHighpass(image):
    kernel_size = 3
    kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    new_image = image
    w,h = image.shape[:2]
    for i in range(w):
        for j in range(h):
            r = 0
            g = 0
            b = 0
            for k in range(kernel_size):
                for l in range(kernel_size):
                    if i-k >= 0 and i-k < w and j-l >= 0 and j-l < h:
                        r += image[i-k][j-l][0] * kernel[k][l]
                        g += image[i-k][j-l][1] * kernel[k][l]
                        b += image[i-k][j-l][2] * kernel[k][l]
            new_image[i][j] = (r,g,b)
    return new_image

def noise(image):
    new_image = image
    w,h = image.shape[:2]
    for i in range(w):
        for j in range(h):
            r,g,b = image[i][j]
            r = r + np.random.randint(-50,50)
            g = g + np.random.randint(-50,50)
            b = b + np.random.randint(-50,50)
            if r < 0:
                r = 0
            if r > 255:
                r = 255
            if g < 0:
                g = 0
            if g > 255:
                g = 255
            if b < 0:
                b = 0
            if b > 255:
                b = 255
            new_image[i][j] = (r,g,b)
    return new_image


# image = Image.open("../test/1_1_Before.jpg")
# image = np.asarray(image)
# # print(image)
# # print('-----------------')
# new_image = np.array(gaussianHighpass(image))
# # print(new_image)
# img = Image.fromarray(new_image)
# img.save('../test/1_1_After.png')