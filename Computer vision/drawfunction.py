import cv2
import numpy as np

img = cv2.imread('lena.jpg', 1)

img = np.zeros([1000, 1000, 3], np.uint8)

img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 2)
img = cv2.arrowedLine(img, (300, 0), (255, 255), (0, 255, 0), 2)
img = cv2.rectangle(img, (500, 300), (300, 200), (0, 5, 255), -1)
img = cv2.circle(img, (200, 500), 150, (200, 100, 0), -1)
font = cv2.FONT_ITALIC
img = cv2.putText(img, 'harley luktar bajs', (100, 300),
                  font, 1, (255, 255, 255), 2)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
