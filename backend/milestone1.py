import numpy as np

def negative(image):
    w,h,d = image.shape[:3]
    new_image = np.zeros((w,h,d), np.uint8)
    if d == 4:
        for i in range(w):
            for j in range(h):
                r,g,b,a = image[i][j]
                new_image[i][j] = (255-r,255-g,255-b,a)
    elif d == 3:
        for i in range(w):
            for j in range(h):
                r,g,b = image[i][j]
                new_image[i][j] = (255-r,255-g,255-b)
    else:
        for i in range(w):
            for j in range(h):
                new_image[i][j] = (255-image[i][j])
    
    return new_image

def grayscale(image):
    w,h,d = image.shape[:3]
    new_image = np.zeros((w,h,d), np.uint8)
    if d == 4:
        for i in range(w):
            for j in range(h):
                r,g,b,a = image[i][j]
                y =round(0.229*r+0.587*g+0.114*b) 
                new_image[i][j] =  new_image[i][j] = (y,y,y,a)
    elif d == 3:
        for i in range(w):
            for j in range(h):
                r,g,b = image[i][j]
                y =round(0.229*r+0.587*g+0.114*b) 
                new_image[i][j] =  new_image[i][j] = (y,y,y)
    else:
        new_image = image
           
    return new_image

def complement(image):
    w,h,d = image.shape[:3]
    new_image = np.zeros((w,h,d), np.uint8)
    if d == 4:
        for i in range(w):
            for j in range(h):
                r,g,b,a = image[i][j]
                new_image[i][j] = (~r,~g,~b,a)
    elif d == 3:
        for i in range(w):
            for j in range(h):
                r,g,b = image[i][j]
                new_image[i][j] = (~r,~g,~b)
    else:
        for i in range(w):
            for j in range(h):
                new_image[i][j] = (~image[i][j])
    return new_image

def rotate90CCW(image):
    w,h,d = image.shape[:3]
    new_image = np.zeros((h,w,d), np.uint8)

    if d == 3 or d == 4:
        for k in range(3):
            for i in range(w):
                for j in range(h):
                    new_image[j][i][k] = image[i][h-j-1][k]
                    if d == 4 and k == 2:
                        new_image[i][j][3] =  image[i][h-j-1][3]
    else:
        for i in range(w):
            for j in range(h):
                new_image[j][i] = image[i][h-j-1]
        
    return new_image

def rotate90CW(image):
    w,h,d = image.shape[:3]
    new_image = np.zeros((h,w,d), np.uint8)

    if d == 3 or d == 4:
        for k in range(3):
            for i in range(w):
                for j in range(h):
                    new_image[j][i][k] = image[w-i-1][j][k]
                    if d == 4 and k == 2:
                        new_image[i][j][3] = image[w-i-1][j][3]
    else:
        for i in range(w):
            for j in range(h):
                new_image[j][i] = image[w-i-1][j]
    return new_image

def flip_vertical(image):
    w,h,d = image.shape[:3]
    new_image = np.zeros((w,h,d), np.uint8)

    if d == 4 or d ==3 :
        for k in range(3):
            for i in range(w):
                for j in range(h):
                    new_image[i][j][k] = image[i][h-j-1][k]
                    if d == 4 and k == 2:
                        new_image[i][j][3] = image[i][h-j-1][3]
    else:
        for i in range(w):
            for j in range(h):
                new_image[i][j] = image[i][h-j-1]
    return new_image

def flip_horizontal(image):
    w,h,d = image.shape[:3]
    new_image = np.zeros((w,h,d), np.uint8)
    
    if d == 4 or d == 3:
        for k in range(3):
            for i in range(w):
                for j in range(h):
                    new_image[i][j][k] = image[w-i-1][j][k]
                    if d == 4 and k == 2:
                        new_image[i][j][3] = image[w-i-1][j][3]
    else:
        for i in range(w):
            for j in range(h):
                new_image[i][j] = image[w-i-1][j]
    return new_image

def zoom_in(image):
    w,h,d = image.shape[:3]
    new_image = np.zeros((w*2,h*2,d), np.uint8)

    for i in range(w):
        for j in range(h):
            new_image[i*2][j*2] = image[i][j]
            new_image[i*2+1][j*2] = image[i][j]
            new_image[i*2][j*2+1] = image[i][j]
            new_image[i*2+1][j*2+1] = image[i][j]
    return new_image

def zoom_out(image):
    w,h,d = image.shape[:3]
    new_image = np.zeros((w//2,h//2,d), np.uint8)

    for k in range(3):
        for i in range(w//2):
            for j in range(h//2):
                temp = (image[i*2][j*2][k] + image[i*2+1][j*2][k] + image[i*2][j*2+1][k] + image[i*2+1][j*2+1][k])//4
                if temp > 255:
                    temp = 255
                if temp < 0:
                    temp = 0
                new_image[i][j][k] = temp
        
    return new_image