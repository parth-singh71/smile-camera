import os
import cv2
from utils import is_smile_inside_face, \
    get_selfie_number, create_dir

# Starting video capture from webcam
capture = cv2.VideoCapture(0)
# getting the last selfie number to determine new file name
num = get_selfie_number()
# specifying the directory where selfies will be saved
dst = "selfies"
# creating the directory if not already exists
create_dir(dst)
# initialing the counter
i = 1
# starting an infinite loop
while True:
    # specifying the breaking condition
    if i == 2:
        break
    else:
        # getting the frame from video
        _, frame = capture.read()
        # making a copy of the frame
        fcopy = frame.copy()
        # converting to grayscale image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # loading openCV's face and smile Haar Cascades
        haar_face = cv2.CascadeClassifier('cascades/face.xml')
        haar_smile = cv2.CascadeClassifier('cascades/smile.xml')
        # detecting face coordinates of the form- (x, y, w, h)
        faces = haar_face.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=50)
        # looping through all faces
        for fx, fy, fw, fh in faces:
            # drawing a green rectangle around the face
            cv2.rectangle(frame, (fx, fy), (fx + fw, fy + fh),
                          (0, 255, 0), thickness=1)
            # labeling the rectangle
            cv2.putText(frame, "Face", (fx, fy - 6),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0, 255, 0), thickness=1)
            # getting the face's roi (region of interest) by cropping out the grayscale img
            face_roi = gray[fy:fy + fh, fx: fx + fw]
            # detecting smile coordinates on the face roi
            smiles = haar_smile.detectMultiScale(
                face_roi, scaleFactor=1.1, minNeighbors=500)
            if not smiles == ():
                # saving the selfie
                cv2.imwrite(f"{dst}/selfie-{num + i}.png", fcopy)
                print("Selfie Captured!!")
                # incrementing the counter
                i += 1
            # looping through all smiles
            for sx, sy, sw, sh in smiles:
                # drawing a yellow rectangle around the smile
                cv2.rectangle(frame, (fx + sx, fy + sy), (fx + sx + sw, fy + sy + sh),
                              (0, 255, 255), thickness=1)
                # labeling the rectangle
                cv2.putText(frame, "Smile", (fx + sx, fy + sy - 6),
                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0, 255, 255), thickness=1)
        # showing the live video to the end user
        cv2.imshow("Smile Selfie Camera", frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break


capture.release()
cv2.destroyAllWindows()
