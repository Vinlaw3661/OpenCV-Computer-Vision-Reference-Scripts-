'''
This script covers colour channels in OpenCV
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

img = cv.imread('Pictures/fox.jpg')
cv.imshow('Normal Image', img)

#Create a blank image with only one colour channel and dimensions equal to original image
blank = np.zeros(img.shape[:2],dtype = 'uint8')

#Split the image into its respective colour channels
b,g,r = cv.split(img)

'''
Display the images. 
The images will be in Grayscale format with the whiter regions representing a larger intensity of 
that specific colour channel'''

cv.imshow('Blue intensity',b)
cv.imshow('Green intensity',g)
cv.imshow('Red intensity',r)

#Merge back the chanensl into the original BGR image
merged = cv.merge([b,g,r,])
cv.imshow('Merged',merged)

#Display each image with intensities represented by the colour itself and not Grayscale
blue = cv.merge([b,blank,blank])
cv.imshow('Blue',blue)

green = cv.merge([blank,g,blank])
cv.imshow('Green',green)

red = cv.merge([blank,blank,r])
cv.imshow('Red',red)


cv.waitKey(0)