import cv2

image = cv2.imread("D:\Python data\image\license_plate_1.jpg", cv2.IMREAD_ANYCOLOR)  # 이미지 불러오기

cvt_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                                  # (입력 이미지, 색상 변환 코드, 출력 채널)
                                                                                     # 변환코드의미: (BGR to GRAY)
cv2.imshow("image", image)
cv2.imshow("cvt_image", cvt_image)                                                   # 변환된 이미지 출력

cv2.waitKey()                                                                        # 화면유지
cv2.destroyAllWindows()                                                              # 화면제거
