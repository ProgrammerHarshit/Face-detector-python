#Importing cv2 (pip install opencv-python)
import cv2

#Captuting video using VideoCapture() method.
#If you have another webcam, then change VideoCapture(0) to VideoCapture(1).
webcam = cv2.VideoCapture(0)

#Starting the loop
while True:
    #Reading each frame caught in your webcam.
    successful_frame_read, frame = webcam.read()

    #Assigning the CascadeClassifier 'haarcascade_frontalface_default.xml' to recognize faces in real time.
    # if you want to download this file, go to (https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml).
    trained_face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    #It searches for the coordinates of where the face is.
    coord = trained_face.detectMultiScale(frame) 

    #This loop draws the rectangle around a face using the coordinates.
    for (x, y, w, h) in coord:
      cv2.rectangle(frame,(x, y), (x+w, x+h),(0, 0, 255), 5)

    #It opens a window named as "Face detector" to open your webcam and detect your face.  
    face_detect = cv2.imshow("Face detector", frame)

    #It will wait until the required key is pressed.
    # If you change cv2.waitKey(1) to cv2.waitKey(0), then you will have to hit spacebar to switch to different frames.
    key = cv2.waitKey(1)

    #if the key 'q' or 'Q' is pressed, then the loop will break, exiting the window
    if key == 81 or key == 113:
       break