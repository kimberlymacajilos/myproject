import cv2
import numpy as np

width, height = 650, 650
canvas = np.zeros((height, width, 3), dtype=np.uint8)

point1 = (175, 100)
point2 = (225, 150)
point3 = (250, 150)
point4 = (275, 150)
point5 = (325, 100)
point6 = (325, 200)
point7 = (175, 200)
point8 = (250, 300)
point9 = (200, 236)
point10 = (300, 236)
point11 = (250, 475)
point12 = (400, 350)
point13 = (375, 475)
point14 = (338, 475)
point15 = (325, 500)

cv2.line(canvas, point1, point2, (255, 0, 0), 2)
cv2.line(canvas, point2, point3, (255, 0, 0), 2)
cv2.line(canvas, point3, point4, (255, 0, 0), 2)
cv2.line(canvas, point4, point5, (255, 0, 0), 2)
cv2.line(canvas, point5, point6, (255, 0, 0), 2)
cv2.line(canvas, point6, point4, (255, 0, 0), 2)

cv2.line(canvas, point1, point7, (255, 0, 0), 2)
cv2.line(canvas, point7, point2, (255, 0, 0), 2)

cv2.line(canvas, point7, point8, (255, 0, 0), 2)
cv2.line(canvas, point8, point6, (255, 0, 0), 2)
cv2.line(canvas, point3, point8, (255, 0, 0), 2)

cv2.line(canvas, point9, point11, (255, 0, 0), 2)
cv2.line(canvas, point11, point10, (255, 0, 0), 2)
cv2.line(canvas, point8, point11, (255, 0, 0), 2)

cv2.line(canvas, point10, point12, (255, 0, 0), 2)
cv2.line(canvas, point12, point13, (255, 0, 0), 2)
cv2.line(canvas, point13, point15, (255, 0, 0), 2)
cv2.line(canvas, point15, point12, (255, 0, 0), 2)
cv2.line(canvas, point11, point14, (255, 0, 0), 2)

cv2.imshow('CAT', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()