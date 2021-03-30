import cv2


image = cv2.imread("D:\Python data\image\license_plate_1.jpg", cv2.IMREAD_ANYCOLOR)
cv2.imshow("Moon", image)
cv2.waitKey()
cv2.destroyAllWindows()

height, width, channel = image.shape
print(height, width, channel)




