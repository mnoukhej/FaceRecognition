import cv2
import os
import pickle
import face_recognition
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendence-6b62b-default-rtdb.firebaseio.com/",    
   'storageBucket': "faceattendence-6b62b.appspot.com"

})


# Importing the students images
folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
    # print(path)
    print(os.path.splitext(path)[0])


    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    
print(studentIds)


def findEncodings(imagesList):
    encodeList = []

    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #img = cv2.resize(img, (160, 160))
        #img = img.reshape(1, 160, 160, 3)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList




print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
print(encodeListKnown)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding complete")


file = open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File Saved Successfully")