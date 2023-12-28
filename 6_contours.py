import cv2 as cv
import numpy as np


img = cv.imread('Pictures/fox.jpg')
cv.imshow('Fox',img)



gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

canny = cv.Canny(gray,125,175)
cv.imshow('Canny Edges', canny)

#Threshholding ,binarises image: below 125 is black above is 255(white)
retval, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

contours, hierachies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours',blank)

cv.waitKey(0)
