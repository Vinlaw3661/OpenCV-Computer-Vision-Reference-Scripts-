'''
This script covers the basics of reading and images and videos in Open CV

Key information:
1. Color mode: unlike most computer programs, OpenCV represents colours in BGR format (as 
opposed to the standard RGB format)
2. When cropping images and dimensions, OpenCV use coordinates (y,x) instead of (x,y)
'''

#Importing OpenCV
import cv2 as cv


#Reading Images
img = cv.imread('Pictures/cat.jpg')

#Show images
cv.imshow('Cat',img)

#waitKey(0) allows image to be displayed indefinitely until we close the window
cv.waitKey(0)

#Shows the image in a new window
cv.imshow()

#Reading Videos
capture = cv.VideoCapture('Videos/climb.mp4')

'''
Videos are treated as images in OpenCV. Each video is cut into individual frames
which can then be passed as images with a certain framerate
'''
#Continous loop to continuously display video until break condition is met
while True:

    #We are only interested in frame, which is the individual frame of the video
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    #This condition allows the video to play until the 'D' key on the keyboard is pressed
    #The condition is that the key should be pressed within 20 milliseconds of a particular frame
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
#Closes the video file or camera device
capture.release()

#Closes all open OpenCV windows
cv.destroyAllWindows()

