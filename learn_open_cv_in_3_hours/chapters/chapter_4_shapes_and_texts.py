import cv2
import numpy as np

AZUL, VERDE, VERMELHO = (255, 0, 0), (0, 255, 0), (0, 0, 255)  # No OPEN CV é BGR em vez de RGB
CIANO, AMARELO = (255, 255, 0), (0, 255, 255)

img = np.zeros((512, 512, 3), np.uint8)
# print(img.shape)
# img[::] = BLUE
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), VERDE, 3)
cv2.rectangle(img, (0, 0), (255, 350), VERMELHO, 2)
cv2.circle(img, (400, 50), 30, CIANO, 5)
cv2.putText(img, " OPENCV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)

cv2.imshow('Image', img)
cv2.waitKey(0)