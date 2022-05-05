import numpy as np
import cv2
from pynput.keyboard import Key,Controller
import pyautogui
import imutils
import time
keyboard=Controller()
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
koni_cascade = cv2.CascadeClassifier('cascade.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("koni.mp4")

while 1:
    ret, img = cap.read()
   # img = pyautogui.screenshot()
    # img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    koniler = koni_cascade.detectMultiScale(gray, 1.3, 5)
    height, width = img.shape[:2]

    cv2.line(img,(int(width/2),height),(int(width/2),int(height/2)),(0,0,255),2)
    # ---------------------------------------------------------'''

    cv2.circle(img, (490, 400), 5, (0, 0, 255), -1)
    cv2.circle(img, (817, 400), 5, (0, 0, 255), -1)

    cv2.circle(img, (0, height - 245), 5, (0, 0, 255), -1)
    cv2.circle(img, (width, height - 245), 5, (0, 0, 255), -1)

    pts1 = np.float32([[490, 400], [817, 400], [100, height - 245], [width-100, height - 245]])
    pts2 = np.float32([[0, 0], [400, 0], [0, 600], [400, 600]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    sonuc = cv2.warpPerspective(img, matrix, (400, 600))
    # ----------------------------------------------------------
    gecici =(0,0,0,0)
    gecici2 = (0, 0, 0, 0)

    for (x, y, w, h) in koniler:
    #if gecici[3] < int(h):
        for (x2, y2, w2, h2) in koniler:
            if abs(h2-h)<35 and abs(x2-x)>250 and h>90 and abs(y2-y)<40 and (x,y,w,h)!=(x2,y2,w2,h2):
                gecici = (x, y, w, h)
                gecici2=(x2, y2, w2, h2)


    uzaklikX_g = abs((width / 2) - (gecici[2] / 2 + gecici[0]))
    uzaklikX_g2 = abs((width / 2) - (gecici2[2] / 2 + gecici2[0]))
    fark=abs(uzaklikX_g2-uzaklikX_g)
    #time.sleep(0.01)
    if uzaklikX_g > uzaklikX_g2 and gecici[0]>gecici2[0]:
        yazi = str(fark) +" birim saga"
        #keyboard.press('d')
       # time.sleep(0.05 * fark / 100)
        #keyboard.release('d')

    elif uzaklikX_g < uzaklikX_g2 and gecici[0]>gecici2[0]:
        yazi = str(fark) +" birim sola"
        #keyboard.press('a')
       # time.sleep(0.05 * fark / 50)
       # keyboard.release('a')

    elif uzaklikX_g < uzaklikX_g2 and gecici[0]<gecici2[0]:
        yazi = str(fark) +" birim saga"
       # keyboard.press('d')
       # time.sleep(0.05 * fark / 50)
       # keyboard.release('d')

    elif uzaklikX_g > uzaklikX_g2 and gecici[0]<gecici2[0]:
        yazi = str(fark) + " birim sola"
       # keyboard.press('a')
      #  time.sleep(0.05 * fark / 50)
      #  keyboard.release('a')


    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, yazi, (int(width / 2), int(height-height/3*2)), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    for (x, y, w, h) in koniler:

        if gecici==(x, y, w, h)  or gecici2==(x, y, w, h) :
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


        #cv2.circle(yol,(int(x+w/2), int(y+h/2)),4, (255, 0, 0), -1)
        uzaklikX = abs((width / 2) - (w / 2 + x))
        uzaklikY = (height) - (y + h)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'x=' + str(int(uzaklikX)) + " y=" + str(int(uzaklikY)), (int(x + w / 2), int(y + h)), font,0.5, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.resizeWindow('Eski video', 1280, 720)
    cv2.imshow('Eski Video', img)
    cv2.imshow('yol', sonuc)



    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

#cap.release()
cv2.destroyAllWindows()