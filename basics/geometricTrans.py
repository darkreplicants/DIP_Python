#!/usr/bin/python2
#

from scipy import misc
from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np


def plot(data, title):
    plot.i += 1
    plt.subplot(2,2,plot.i)
    plt.imshow(data)
    plt.gray()
    plt.title(title)


# Lena 8 bits image
lena = misc.lena()

# Basic Transfornations

lena = misc.lena()
lx, ly = lena.shape
# Cropping
cropLena = lena[lx / 4: - lx / 4, ly / 4: - ly / 4]
# up <-> down flip
flip_udLena = np.flipud(lena)
# rotation
rotateLena = ndimage.rotate(lena, 45)
rotateLenaNoreshape = ndimage.rotate(lena, 45, reshape=False)

# Display images on the screen
plot.i = 0
plot(cropLena, 'Crop')
plot(flip_udLena, 'Flip Ud')
plot(rotateLena, 'Rotate')
plot(rotateLenaNoreshape, 'Rotate No Reshape')

plt.show()
