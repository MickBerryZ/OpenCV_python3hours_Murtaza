import cv2

img = cv2.imread("Resources/torres.jpeg")
print(img.shape)

imgResizeS = cv2.resize(img,(640,480))
print(imgResizeS.shape)

imgResizeB = cv2.resize(img,(3000,2000))
print(imgResizeB.shape)

while True:
    cv2.imshow("Image", img)
    cv2.imshow("ResizeS", imgResizeS)
    cv2.imshow("ResizeB", imgResizeB)
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        break