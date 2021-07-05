import cv2
import winsound
cam=cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame1=cam.read()
    ret,frame2=cam.read()
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilate=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1,contours,-1,(0,0,255),2)
    for c in contours:
        if cv2.contourArea(c)<7000:
            continue
        x,y,w,h=cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),2)
        winsound.Beep(4000,100)
        winsound.PlaySound("alert.wav",winsound.SND_ASYNC)
    if cv2.waitKey(10)==ord("q"):
        break
    cv2.imshow("camera",frame1)
