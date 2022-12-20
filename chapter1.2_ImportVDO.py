import cv2

cap = cv2.VideoCapture("Resources/jaypark_test.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break
    