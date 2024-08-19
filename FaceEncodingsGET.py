import cv2 as cv
import face_recognition as fr

img1 = "refImage.jpg"
img2 = "refImageCam.jpg"

def faceEncode(image):
    img = cv.imread(image)
    faceEnc = fr.face_encodings(img)
    return faceEnc[0]

def cmpFaces(enc1,enc2):
    Check = fr.compare_faces([enc1],enc2)[0]
    return Check

enc1 = faceEncode(img1)
enc2 = faceEncode(img2)

faceCheck = cmpFaces(enc1,enc2)
print("Is same: ",faceCheck)
