import cv2
import numpy as np
print("test")

background = cv2.imread("safari.jpeg")

foreground = cv2.imread("giraffe.jpeg")

#get color of background green screen

print(foreground.shape)     #size of pic,  height, width

picWidth = foreground.shape[1]
picHeight = foreground.shape[0]

print(foreground[40,40])

resized = cv2.resize(background,(picWidth,picHeight))



for i in range(0, picWidth):
    for j in range(0, picHeight):
        pixel = foreground[j, i]
        if np.any(pixel == [1, 255, 0]): #green color       #convert pixel to list to compare with [28, 255, 76]
            foreground[j,i] = resized[j,i] #if its green, it will get same pixel as background

cv2.imwrite("outputPic.jpeg", foreground)
print("DONE")