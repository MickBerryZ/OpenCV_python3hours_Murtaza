import cv2
print("Package Imported")

img = cv2.imread("Resources/torres.jpeg")

cv2.imshow("output",img)
cv2.waitKey(5000) # if set 1000, that means 1 secondq and 0 is forever