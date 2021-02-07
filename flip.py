import cv2 as cv
import numpy as np

img = cv.imread('/home/darshan/Darshan/Work/dog.jpg')
cv.imshow('dog', img)

# Flipping 
# 0 -> x axis flip
# 1 -> y axis flip 
# -1 -> x and y axis flip together

flip = cv.flip(img, -1)
cv.imshow('Flip_dog', flip)
cv.waitKey(0)