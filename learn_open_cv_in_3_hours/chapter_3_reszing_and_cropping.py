import cv2
import numpy as np

img = cv2.imread('../resources/lambo.PNG')
print(img.shape)
# (462, 623, 3) -> (altura, largura, número de canais de cor, no caso 3 pq é rgb)

img_resize = cv2.resize(img, (300, 200))
print(img_resize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
# cv2.imshow("Image Resize", img_resize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)
