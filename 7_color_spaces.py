'''
This script covers hiw to convert between color spaces (modes) in OpenCV
'''
import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('Pictures/fox.jpg')

#BGR to GRAYSCALE
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

#BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#BGR to RGB. OpenCV inverts the color for BGR when converting to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

#To change from GRAYSCALE to any other channel that is not BGR, you must first convert to
#BGR and then to another channel

plt.imshow(rgb)
plt.show()

plt.imshow(img)
plt.show()

cv.waitKey(0)