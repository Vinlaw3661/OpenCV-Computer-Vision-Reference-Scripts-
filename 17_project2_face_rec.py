import numpy as np 
import cv2 as cv 
import os


#Load face recognizer
haar_cascade = cv.CascadeClassifier('haar_face.xml')

#Load label names
dir = r'C:\Users\vmude\Desktop\AI\OpenCV\Faces\train'
people = []
for folder in os.listdir(dir):
    people.append(folder)

#Load feature images and labels in case we want to use them for troubleshooting
features = np.load('features.npy' , allow_pickle=True)
labels = np.load('labels.npy')

#Load trained face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

#Load validation image
img = cv.imread(r'C:\Users\vmude\Desktop\AI\OpenCV\Faces\val\ben_afflek\2.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)

#Predict each face detected by Haar Cascade
for (x,y,w,h) in faces_rect:

    faces_roi = gray[y:y+h,x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)

    print(f'Label predicted is {people[label]} with a confidence of {confidence}')
    cv.putText(img,f"{people[label]}",(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),1)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv.imshow('Predicted Face', img)
    cv.imshow('Gray', gray)
    cv.waitKey(0)

