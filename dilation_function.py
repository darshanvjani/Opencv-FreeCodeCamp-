import cv2

dog = cv2.imread('/home/darshan/Darshan/Work/dog.jpg')

blured_dog = cv2.blur(dog,(3,3),cv2.BORDER_DEFAULT) #blur to reduce noice
cannyimg = cv2.Canny(blured_dog,150,200)    #canny to find edges

dilated_dog = cv2.dilate(cannyimg,(3,3),iterations=7) #to strengthen weak edges 


cv2.imshow('without_dilation_dog',cannyimg) #without dilation
cv2.imshow('with_dilated_dog',dilated_dog)  #with dilation
cv2.waitKey()