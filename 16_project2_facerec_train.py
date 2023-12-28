import cv2 as cv
import os
import numpy as np 



people = []

#Create main path variable
dir = r'C:\Users\vmude\Desktop\AI\OpenCV\Faces\train'

#Haar cascade will be used to extract only the image region with the faces
haar_cascade = cv.CascadeClassifier('haar_face.xml')

#Create a list of the people whose faces are to be recognized
for folder in os.listdir(dir):
    people.append(folder)


features = []
labels = []

#Function to create train data: features and labels
def create_train_data():

    #Loop over each folder
    for person in people:

        path = os.path.join(dir,person)
        label = people.index(person)

        #Loop over each image in a folder
        for image in os.listdir(path):

            image_path = os.path.join(path,image)
            img = cv.imread(image_path)
            gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)

            #Loop over each face in an image 
            for (x,y,w,h) in faces_rect:

                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train_data()

#Convert features and labels into numpy arrays for faster computations
features = np.array(features, dtype = 'object')
labels = np.array(labels)

np.save('features.npy',features)
np.save('labels.npy', labels)

#Create Face Recognizer and Train it on features and labels
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)

#Save Trained model
face_recognizer.save('face_trained.yml')

