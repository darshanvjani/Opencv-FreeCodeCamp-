import cv2 as cv
import numpy as np

img = cv.imread('/home/darshan/Darshan/Work/dog.jpg')
cv.imshow('dog', img)

# Rotation Function
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 90)
cv.imshow('Rotated_dog', rotated)


cv.waitKey(0)