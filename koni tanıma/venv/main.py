import cv2
import imageio
import math
yuzCascade = cv2.CascadeClassifier('cascade.xml')





def detect(frame):
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = yuzCascade.detectMultiScale(gri, 1.3, 5)
    height, width = gri.shape[:2]
    cv2.line(frame,(int(width/2),int(height/2)),(int(width/2),int(height)),(0,255,0),2)

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        uzaklikX=abs((width/2)-(w/2+x))
        uzaklikY=(height)-(y+h)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'x=' + str(int(uzaklikX))+" y="+str(int(uzaklikY)), (int(x+w/2), int(y+h)), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)



    return frame

reader = imageio.get_reader('koni2.mp4')

fps = reader.get_meta_data()['fps']
writer = imageio.get_writer('output2.mp4', fps=fps)

for i, frame in enumerate(reader):
    frame = detect(frame)
    writer.append_data(frame)
    print(i)
writer.close()
