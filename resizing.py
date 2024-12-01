import cv2

img = cv2.imread('BackgroundImages/2.jpg')
img = cv2.resize(img, (640, 480))
# Uncomment below lines to display the image if needed
# cv2.imshow("img", img)
# cv2.waitKey(0)
cv2.imwrite("2.jpg", img)
