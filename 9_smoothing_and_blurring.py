'''
This script covers smoothing and blurring images in OpenCV
'''
import cv2 as cv
import numpy as np 

img = cv.imread('Pictures/fox.jpg')
cv.imshow('Normal Image', img)

#Average Blur
avg = cv.blur(img,(7,7))
cv.imshow("Average",avg)
#Gaussian Blur
gaus = cv.GaussianBlur(img,(7,7),3)
cv.imshow("Gaussian",gaus)

#Median Blur
med = cv.medianBlur(img,7)
cv.imshow("Median", med)

#Bilateral Blur
bilateral = cv.bilateralFilter(img, 5,50,50,)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)