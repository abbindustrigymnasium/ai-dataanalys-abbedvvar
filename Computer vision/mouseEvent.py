import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)


def mouseClick(event, x, y, flags, params):
    font = cv2.FONT_ITALIC
    if event == cv2.EVENT_LBUTTONDOWN:
        XY = str(x) + ', ' + str(y)
        cv2.putText(frame, XY, (x, y), font, 1, (255, 0, 255), 3)
        cv2.imshow('frame', frame)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = frame[y, x, 0]
        red = frame[y, x, 1]
        green = frame[y, x, 0]
        colorPick = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(frame, colorPick, (x, y), font, 0.4, (0, 255, 255), 1)
        cv2.imshow('frame', frame)


# frame = np.zeros((1080, 1080, 3), np.uint8)
frame = cv2.imread('lena.jpg', 1)
cv2.imshow('frame', frame)

cv2.setMouseCallback('frame', mouseClick)

cv2.waitKey(0)
cv2.destroyAllWindows()
