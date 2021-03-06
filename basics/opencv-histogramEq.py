import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/lena.png',0)

equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imshow('Eq',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite('res.png',res)

