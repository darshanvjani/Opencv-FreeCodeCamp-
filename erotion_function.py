import cv2

dog = cv2.imshow('/home/darshan/Darshan/Work/dog.jpg')

erode_image = cv2.erode(dog,(7,7),itenrations=3)
cv2.imshow()