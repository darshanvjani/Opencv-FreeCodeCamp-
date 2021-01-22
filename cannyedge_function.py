import cv2
dog_image = cv2.imread('/home/darshan/Darshan/Work/prototyping_1.jpg')

cannyimg = cv2.Canny(dog_image,100,150) #cannyedge detection function

cv2.imshow('canny_edge',cannyimg) 

#NOW WE WILL REMOVE CERTAIN DEGREE OF NOISE BY BLURING IMAGE AND AGAIN FINGIND CANNY EDGE OF IT


blured_dog = cv2.blur(dog_image,(7,7),cv2.BORDER_DEFAULT) #cannyedge detection function

blured_cannyimg = cv2.Canny(blured_dog,125,175) #blure function with 7X7 kernal size
cv2.imshow('blured_canny_edge',blured_cannyimg) 
cv2.waitKey(0)