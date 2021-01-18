import cv2
dog = cv2.imread('/home/darshan/Darshan/Work/dog.jpg')
#rescale function
def rescaleframe(frame,scale):
    width =  int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height) 
    
    return cv2.resize(frame,dimension,interpolation=cv2.INTER_AREA)
#RESCALING VIDEOS

scaled_dog = rescaleframe(dog,0.50)
cv2.imshow('org_dog',dog)  #Original
cv2.imshow('scaleddog',scaled_dog)  #Rescaled
cv2.waitKey(0)
#RESCALING VIDEOS

#read videos
capture = cv2.VideoCapture('/home/darshan/Darshan/Work/cat.mp4')

#show continuous frames of Video
while True:
    _ , frame = capture.read()
    rescaled = rescaleframe(frame,0.75)

    cv2.imshow('cat',frame) #Original
    cv2.imshow('cat',rescaled) #Rescaled

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()



    

