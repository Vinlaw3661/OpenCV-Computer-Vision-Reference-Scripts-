import numpy as np
import matplotlib.pyplot as plt 
import cv2 as cv 

img = cv.imread('Pictures/fox.jpg')
cv.imshow('Normal',img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),300,255,-1)
mask = cv.bitwise_and(gray,gray,mask = circle)

cv.imshow('Mask',mask)

hist = cv.calcHist([gray],[0],mask,[256],[0,256])

plt.figure()
plt.title('Grayscale Pixel Intensity')
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of Pixels')
plt.plot(hist)
plt.xlim([0,256])
plt.show()


mask2 = cv.bitwise_and(img,img,mask = circle)
cv.imshow('Mask2', mask2)


plt.figure()
plt.title('Pixel Color Intensity')
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of Pixels')

colors = ['b','g','r']
for i,col in enumerate(colors):

    hist2 = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist2, color = col)
    plt.xlim([0,256])

plt.show()

hist2 = cv.calcHist([img], [2])
cv.waitKey(0)