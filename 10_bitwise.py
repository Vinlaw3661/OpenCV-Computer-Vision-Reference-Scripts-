import cv2 as cv
import numpy as np 

blank = np.zeros((400,400), dtype = 'uint8')

#Create shapes that will be used for bitwise operations
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle', circle)

#AND covered only by both
bit_and = cv.bitwise_and(rectangle,circle,)

#OR - covered by all 
bit_or = cv.bitwise_or(rectangle,circle)

#XOR not covered by both, only covered by either
bit_xor = cv.bitwise_xor(rectangle,circle)

#NOT
bit_not = cv.bitwise_not(rectangle)

cv.imshow('AND', bit_and)
cv.imshow('OR', bit_or)
cv.imshow('XOR', bit_xor)
cv.imshow('NOT', bit_not)

cv.waitKey(0)