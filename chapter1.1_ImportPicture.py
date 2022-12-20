import cv2
print("Package Imported")

img = cv2.imread("Resources/torres.jpeg")

while True:
    cv2.imshow("output",img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # if set 1000, that means 1 secondq and 0 is forever
        break