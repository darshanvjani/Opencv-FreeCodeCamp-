import cv2
dog_image = cv2.imread('/home/darshan/Darshan/Work/dog.jpg')

blur_dog = cv2.GaussianBlur(dog_image,(7,7),cv2.BORDER_DEFAULT) #function to blur the image so that to decrease the noise

cv2.imshow('dog',blur_dog)
cv2.waitKey(0)