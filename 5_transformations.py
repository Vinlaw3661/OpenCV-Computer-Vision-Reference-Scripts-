'''
This script covers image transformations in OpenCV as an extension of the rescale script
'''
import cv2 as cv
import numpy as np

img = cv.imread('Pictures/fox.jpg')
cv.imshow('Fox',img)


#Translation
#Using -x translates to the left, and -y trnaslates upwards
def translate(image,x,y):

    #Create a translation matri to translate image in x and y directions
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (image.shape[1],image.shape[0])
    return cv.warpAffine(image,transMat,dimensions)


translated = translate(img,20,50)
cv.imshow('Translated',translated)

#Rotation, positive angle counter clockwise, negative clockwise
def rotate(image,angle,rotPoint = None):
    height,width = image.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    #Dimensions of final image after rotation
    dimensions = (width,height)
    
    #Create a rotation matrix to be used for rotation
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,scale = 1.0)

    return cv.warpAffine(image,rotMat,dimensions)

rotated = rotate(img,45)
cv.imshow('Rotated',rotated)

#Flipping image
vertical = cv.flip(img,0)
cv.imshow('Vertical', vertical)

horizontal = cv.flip(img,1)
cv.imshow('Horizontal', horizontal)

#Flips in both horizaontal and vertical directions
both = cv.flip(img,-1)
cv.imshow('Vertical and Horizontal', both)

cv.waitKey(0)