import cv2
import datetime
cap = cv2.VideoCapture(0)

cap.set(3, 3840)
cap.set(4, 2160)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_ITALIC
        date = str(datetime.datetime.now())

        frame = cv2.putText(frame, date, (30, 30),
                            font, 1, (255, 255, 255), 2)
        frame = cv2.putText(frame, 'harley luktar bajs', (100, 300),
                            font, 1, (255, 255, 255), 2)
        frame = cv2.rectangle(frame, (200, 200), (500, 500), (255, 0, 0), 3)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
