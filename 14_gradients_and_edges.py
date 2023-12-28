import numpy as np 
import cv2 as cv 

img = cv.imread('Pictures/fox.jpg')
cv.imshow('Normal',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#Sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
sobel = cv.bitwise_or(sobelx,sobely)
sobelb = cv.Sobel(gray,cv.CV_64F,1,1)
cv.imshow('SobelX', sobelx)
cv.imshow('SobelY', sobely)
cv.imshow('Combined Sobel', sobel)
cv.imshow('Sobel Both', sobelb)

cv.waitKey(0)