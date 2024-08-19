#importing required modules
import cv2 as cv
import face_recognition as fr

#defining function that returns face encodings
def findFaceEncoding(Image):
    faceEnc = fr.face_encodings(Image)
    return faceEnc[0]

#defining function that compares two faces
def compareFaces(Im1,Im2):
   sameCheck = fr.compare_faces([Im1],Im2)[0]
   return sameCheck

#capturing video through web camera
cap = cv.VideoCapture(0)

#read reference image
img = cv.imread("refImage.jpg")

#Face encoding of source image
Im1 = findFaceEncoding(img)

#initialize frame count as 0
frameCount = 0

try:

    while True:

        #read frames from web camera
        ret,frame = cap.read()

        #converting frame from BGR to RGB
        rgbFrame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)

        #if frames not received program ends
        if not ret:
            print("Can't receive frames. Quiting....!")

        #checks for face matches every 30s
        if frameCount%30 == 0:
            Im2 = findFaceEncoding(rgbFrame)
            Check = compareFaces(Im1,Im2)
            if Check:
                print("SAME")
            else:
                print("NOT SAME")
                
        #displays camera output    
        cv.imshow("WEB CAMERA",frame)

        #program ends when 'q' key pressed
        if cv.waitKey(1) == ord("q"):
            break

        frameCount+=1

except:
    print("Can't Open Camera....!")

#Releasing camera object
cap.release()
cv.destroyAllWindows()
