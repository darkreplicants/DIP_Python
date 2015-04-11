#!/usr/bin/python2

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc

def plot(data, title):
        plot.i += 1
        plt.subplot(2,2,plot.i)
        plt.imshow(data)
        plt.gray()
        plt.title(title)

# Load Lena Image
l = misc.lena()

# Create a new image applying noise to Lena
noisy = l + 0.4 * l.std() * np.random.random(l.shape)

# Filter image with Gaussian Filter
gauss_denoised = ndimage.gaussian_filter(noisy, 2)

# Filter with Median Filter
med_denoised = ndimage.median_filter(noisy, 3)

plot.i = 0
plot(l,'Original')
plot(noisy,'Noise Added')
plot(gauss_denoised,'Gaussian Filter')
plot(med_denoised,'Median Filter')
plt.show()
