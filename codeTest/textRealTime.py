import cv2

cam = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
while True:
    ok,img = cam.read();

    cv2.putText(img , "center", (10, 500), font, 4, (0, 255, 0), 10)

    cv2.imshow('frame',img)
    ch = 0xFF & cv2.waitKey(1)
    if ch == 27:
        break
cv2.destroyAllWindows()
