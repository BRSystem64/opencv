import numpy as np
import cv2 as cv 

img = cv.imread('../../img/torre-pisa.jpg', cv.IMREAD_GRAYSCALE)

cv.imshow('torre de pisa', img)

cv.waitKey(0)
cv.destroyAllWindows()