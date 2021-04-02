from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time


import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt
# TODO Show image function


Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


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


def runalgo(path):
    print(path)
    algo(path)




class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        saving_file = "IMG_{}.png".format(timestr)
        print("Captured")

        # Call algo

        runalgo(saving_file)


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()