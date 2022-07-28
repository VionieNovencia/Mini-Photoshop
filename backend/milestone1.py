import numpy as np

def negative(image):
    w,h = image.shape[:2]
    new_image = image
    for i in range(w):
        for j in range(h):
            r,g,b = image[i][j]
            new_image[i][j] = (255-r,255-g,255-b)
    return new_image

def grayscale(image):
    w,h = image.shape[:2]
    new_image = image
    for i in range(w):
        for j in range(h):
            r,g,b = image[i][j]
            y =round(0.229*r+0.587*g+0.114*b) 
            new_image[i][j] = (y,y,y)
    return new_image

def complement(image):
    w,h = image.shape[:2]
    new_image = image
    for i in range(w):
        for j in range(h):
            r,g,b,a= image[i][j]
            new_image[i][j] = (255-r,255-g,255-b,a)
    return new_image

def rotate90CCW(image):
    w,h = image.shape[:2]
    new_image = np.zeros((h,w,3), np.uint8)

    for k in range(3):
        for i in range(w):
            for j in range(h):
                new_image[j][i][k] = image[i][h-j-1][k]
        
    return new_image

def rotate90CW(image):
    w,h = image.shape[:2]
    new_image = np.zeros((h,w,3), np.uint8)

    for k in range(3):
        for i in range(w):
            for j in range(h):
                new_image[j][i][k] = image[w-i-1][j][k]
    return new_image

def flip_horizontal(image):
    w,h = image.shape[:2]
    new_image = np.zeros((w,h,3), np.uint8)

    for k in range(3):
        for i in range(w):
            for j in range(h):
                new_image[i][j][k] = image[i][h-j-1][k]
            
    return new_image

def flip_vertical(image):
    w,h = image.shape[:2]
    new_image = np.zeros((w,h,3), np.uint8)

    for k in range(3):
        for i in range(w):
            for j in range(h):
                new_image[i][j][k] = image[w-i-1][j][k]
        
    return new_image

def zoom_out(image):
    w,h = image.shape[:2]
    new_image = []

    r = 0
    for i in range(1,w*2+1):
        temp = []
        c = 0
        for j in range(1,h*2+1):
            value= image[r][c]
            if j%2 == 0:
                c+=1
            temp.append(value)
        if i%2 == 0:
            r+=1
        new_image.append(temp)
        
    return new_image

