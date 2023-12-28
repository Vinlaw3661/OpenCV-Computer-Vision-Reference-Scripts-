'''
This script covers the basics of rescaling videos and images in OpenCV
'''
import cv2 as cv

capture = cv.VideoCapture('Videos/climb.mp4')

#Only works for live video
def changeRes(height,width):
    capture.set(4,height) #4 references height
    capture.set(3,width) #3 references width

#Works for images, video and live video
def rescaleFrame(frame, scale = 0.75):

    #Scale determines the percent change. In this case 75% of original size
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width,height)

    #cv.INTER_AREA is the interpolation technique used. It is mainly used when scaling down images
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA) 

while True:

    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Resized Video', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()
        



