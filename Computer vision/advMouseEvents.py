import numpy as np
import cv2


def draw(event, x, y, flags, params):
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(frame, (x, y), 5, (155, 0, 255), -1)
        cv2.imshow('frame', frame)


def mouseClick(event, x, y, flags, params):
    font = cv2.FONT_ITALIC
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.setMouseCallback('frame', draw)
        cv2.circle(frame, (x, y), 5, (155, 0, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(frame, points[-1], points[-2], (255, 0, 255), 3)
        cv2.imshow('frame', frame)

    if event == cv2.EVENT_RBUTTONDOWN:
        points.clear()


# frame = np.zeros((1080, 1080, 3), np.uint8)
frame = cv2.imread('lena.jpg', 1)
cv2.imshow('frame', frame)

points = []
cv2.setMouseCallback('frame', mouseClick)

cv2.waitKey(0)
cv2.destroyAllWindows()
