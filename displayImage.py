#!/usr/bin/python2
from scipy import misc
import matplotlib.pyplot as plt


l = misc.lena()
misc.imsave('lena.png', l)
plt.imshow(l)
plt.imshow(l, cmap=plt.cm.gray, vmin=30, vmax=200)
plt.axis('off')
plt.show()
