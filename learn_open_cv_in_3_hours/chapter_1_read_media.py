import cv2

caminho_video = "../resources/test_video.mp4"
# cap = cv2.VideoCapture(caminho_video)
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
leave_program = lambda: cv2.waitKey(1) & 0xFF == ord('q')

while True:
    succes, img = cap.read()
    cv2.imshow("Video", img)
    if leave_program():
        break
