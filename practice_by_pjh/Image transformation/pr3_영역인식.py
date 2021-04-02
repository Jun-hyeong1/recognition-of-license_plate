import cv2

image = cv2.imread("D:\Python data\image\license_plate_1.jpg", cv2.IMREAD_ANYCOLOR)  # 이미지 불러오기


gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)                                       # 색상변환(Gray)

ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

for i in range(len(contours)):
    cv2.drawContours(image, [contours[i]], 0, (0, 0, 255), 2)
    cv2.putText(image, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
    print(i, hierarchy[0][i])
    cv2.imshow("image", image)
    cv2.waitKey(0)

cv2.destroyAllWindows()