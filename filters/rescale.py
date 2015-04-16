#!/usr/bin/python2
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndimage
from scipy import misc

def plot(data, title):
    plot.i += 1
    plt.subplot(2,2,plot.i)
    plt.imshow(data)
    plt.gray()
    plt.title(title)

# Using the original to get the same results
im = misc.imread('../images/building.jpg')

# Image converted to double with max value of 1
imMapped = np.array(im)/255.0
plot.i = 0
plot(imMapped, 'Original')

# Create a Low Pass Filter 3x3
lpf3 = np.ones((3,3))/9.0

# Filtering Image: Convolute image mapped with matrix filter
imFiltered = ndimage.convolve(imMapped, lpf3, mode='nearest')


# Down Sampling image
#

# Helper variables to make down sampling
for nRows in range(0,179):
    evenRows[nRows]=2*nRows+1

for nColumns in range(0,239):
    evenColumns[evenColumns]=2*nColumns+1

# Down Sampling original image
resizeImage=imMapped(evenRows,evenColumns)

# Down Sampling LPFiltered image
resizeImageF=imfiltered(evenRows,evenColumns)

# Display both images to compare
plot(resizeImage, 'Down Sampled')
plot(resizeImageF, 'Down Sampled LPF')

mse3 = np.sum(np.power(imFiltered-imMapped,2))/np.size(imMapped)

# PSNR = 10*np.log10(np.power(MAXi,2)/MSE);
# MAXI is the maximum possible pixel value of the image. 
# because of image is converted to double and pixel value
# is  map value to 0 - 1 MAXI is equal to 1

psnr3 = 10*np.log10(np.power(1.0,2)/mse3);

print psnr3

plot(imFiltered, '3x3 low-pass')
plt.show()
