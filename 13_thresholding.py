import cv2 as cv 

img = cv.imread('Pictures/fox.jpg')
cv.imshow('Normal', img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Simple thresholding
retval, thresh1 = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Simple Thresholding', thresh1)

#Inverse thresholding
retval, thresh2 = cv.threshold(gray,125,255,cv.THRESH_BINARY_INV)
cv.imshow('Inverse Simple Thresholding', thresh2)

#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive', adaptive_thresh)
cv.waitKey(0)
