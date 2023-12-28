'''
This script covers the essential functions in OpenCV
'''
import cv2 as cv

img = cv.imread('Pictures/fox.jpg')
cv.imshow('Color', img)

#Change BGR to Grayscale:
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)

#Blur, used to reduce detail in images
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascade used to find the edges of an image
#You can reduce the edges by passing in a blurred image
canny = cv.Canny(img,125,175)
cv.imshow('Canny',canny)

#Dilating image 
#Dilates the edges of the image or the image itself
dilate = cv.dilate(canny,(7,7), iterations = 3)
cv.imshow('Dilate', dilate)

#Erode reverses the dilation to get back to the original edge cascaded image
eroded = cv.erode(dilate,(7,7), iterations = 3)
cv.imshow('Eroded',eroded)

#Resizing, cv.INTER_AREA is good for making picture smaller. 
#For upscaling, use cubic and linear to retain quality
resized = cv.resize(img, (200,200), cv.INTER_AREA)
cv.imshow('Resized',resized)

#Cropping crops image to the specified width and length dimensions
cropped = img[50:100, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)