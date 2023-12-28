import cv2 as cv 

img = cv.imread('Pictures/face.webp')
#cv.imshow('Face',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray Face', gray)

haar = cv.CascadeClassifier('haar_face.xml')

#Face Detection implementation for images
#returns the rectangular coordinates corresponding to a face
faces_rect = haar.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=3)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


print(f'Number of faces detecetd: {len(faces_rect)}')

cv.imshow('Detected Face', img)
cv.waitKey(0)

#Face Detection Implementation for video feed
capture = cv.VideoCapture(0)

while True:
    
    isTrue, frame = capture.read()
    gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces_rect2 = haar.detectMultiScale(gray_frame,scaleFactor=1.1, minNeighbors=3)
    for (x,y,w,h) in faces_rect2:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        #if len(faces_rect2) > 0:
        cv.putText(frame,'Face detected',(x+ w//2,y),cv.FONT_HERSHEY_PLAIN,1.0,(0,255,0))
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()

