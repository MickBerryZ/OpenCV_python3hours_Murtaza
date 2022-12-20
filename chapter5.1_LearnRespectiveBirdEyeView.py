import cv2
import numpy as np

img = cv2.imread("Resources/card.jfif")

imgResizeS = cv2.resize(img,(640,480))
print(imgResizeS.shape)

width, height = 250,350

pts1 = np.float32([[222,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(imgResizeS, matrix, (width, height))

while True:
    
    cv2.imshow("Images", imgResizeS)
    cv2.imshow("Output", imgOutput)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break