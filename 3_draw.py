'''
This script covers the basics of drawing shapes and writing text in OpenCV
'''
import cv2 as cv
import numpy as np

#Create blank canvas of 500x500 with 3 colour channels
blank = np.zeros((500,500,3), dtype='uint8') #dtype = 'uint8' specifies that the data type is an image
cv.imshow('Blank', blank)

#Assign the values for each of the 3 color channels for specific pixels across and along
#Start by selecting image area using list slicing and assign color in the form of (Blue, Green, Red)
blank[100:200,200:300] = 0,255,0
cv.imshow('Green',blank)

#Draw a rectangle(img,point1,point2,color,thickness)
#For circle(img,point,radius,color,thickness)
#For line(img,point1,point2,color,thickness)
cv.rectangle(blank,(0,0),(250,250),(255,0,0),thickness=cv.FILLED) #cv.FILLED works the same as -1
cv.imshow('Rectangle',blank)

#Writing text to an image (img,text,point,font,scale,color,thickness)
cv.putText(blank,"Hello Vinlaw",(0,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(250,0,0),2)
cv.imshow("Text",blank)
cv.waitKey(0)