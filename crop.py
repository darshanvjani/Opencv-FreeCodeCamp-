import cv2 as cv
import numpy as np

img = cv.imread('/home/darshan/Darshan/Work/dog.jpg')
cv.imshow('dog', img)

# Cropping (matrix slicing)
cropped = img[200:400, 300:400]
cv.imshow('Cropped_dog', cropped)


cv.waitKey(0)