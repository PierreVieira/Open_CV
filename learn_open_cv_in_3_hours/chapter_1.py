import cv2
print('Package Imported')

img = cv2.imread("../Resources/my_imgs/pierre_vieira_13_anos.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)
