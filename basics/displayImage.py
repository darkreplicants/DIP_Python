#!/usr/bin/python2
import scipy.misc
import matplotlib.pyplot as plt


lena8b = scipy.misc.lena()
scipy.misc.imsave('../images/lena8b.png', lena8b)
plt.imshow(lena8b)
plt.imshow(lena8b, cmap=plt.cm.gray, vmin=30, vmax=200)
plt.axis('off')
plt.show()
