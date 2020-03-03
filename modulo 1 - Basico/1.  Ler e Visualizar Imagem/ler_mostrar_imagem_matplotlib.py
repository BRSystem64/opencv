import numpy as np
import cv2 as cv 
from matplotlib import pyplot as plt 

img = cv.imread('../img/torre-pisa.jpg')


# Conversão de BGR para RGB
img = img[:, :, ::-1]

plt.imshow(img)
plt.title('Torre de Pisa')

plt.show()