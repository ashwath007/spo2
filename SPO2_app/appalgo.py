import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt
# TODO Show image function


def max_rgb_filter(image):
    (B, G, R) = cv.split(image)
    M = np.maximum(np.maximum(R, G), B)
    R[R < M] = 0
    G[G < M] = 0
    B[B < M] = 0

    return cv.merge([B, G, R])


def dim(bgr_planes):
    if not type(bgr_planes) == list:
        return []
    return [len(bgr_planes)] + dim(bgr_planes[0])



def algo(image):
    data_pic = cv.imread("./"+image)
    cv.imshow('image',data_pic)
    
    
    # Reading Dimensions


    data_pic_red = data_pic[:,:,1]
    filtered_pic = max_rgb_filter(data_pic)


    bgr_planes = cv.split(data_pic)
    dim_result = dim(bgr_planes)


    # Filter 

    RED = plt.hist(bgr_planes[2].ravel(),256,[0,256]) 
    BLUE = plt.hist(bgr_planes[0].ravel(),256,[0,256]) 


    img_m = max(RED[0])/(max(RED[0])+BLUE[0][50])
    print("SPO2 : {}".format(img_m*100))

    cv.waitKey(0)
    cv.destroyAllWindows()