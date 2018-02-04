import cv2
img = "/home/uawsscu/PycharmProjects/ProFinal/hotdog-or-not-hotdog-master/test/h1.jpg"

image = cv2.imread(img)
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(image, "center", (10, 500),font, 4, (255, 255, 255), 10)
cv2.imshow("Image", image)
cv2.waitKey(0)