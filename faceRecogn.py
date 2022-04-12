# from tabnanny import check
import cv2, time
# import pyautogui

#get screen resolution:
# width, height= pyautogui.size()

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read ()
    # time.sleep(1)

    grey_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey_frame, scaleFactor = 1.05, minNeighbors=5)
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    # frame_resized = cv2.resize(frame, (width,height),interpolation = cv2.INTER_AREA)
    cv2.namedWindow("Tytul");
    cv2.moveWindow("Tytul", 50,50);    
    cv2.imshow("Tytul",frame)
    key = cv2.waitKey(1)
    if key == ord ('q'):
        break

video.release()
cv2.destroyAllWindows()