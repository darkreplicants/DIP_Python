#!/usr/bin/python2
#
# This script reads from a file "linux.png" an image
# shows some images properties at command line and
# shows image on the screen
#

from scipy import misc
import matplotlib.pyplot as plt

def plot(data, title):
    plot.i += 1
    plt.subplot(2,2,plot.i)
    plt.imshow(data)
    plt.gray()
    plt.title(title)


# Read image from file
lena = misc.imread('../images/lena.png')

# Get each RGB channel
lenaR = lena[:,:,0]
lenaG = lena[:,:,1]
lenaB = lena[:,:,2]


# Display on CMD some image properties
print "Image type: ", type(lena)
print "Image size: ",lena.size
print "Image shape: ",lena.shape
print "Image type: ", lena.dtype 

# Display image on the screen
plot.i = 0
plot(lena, 'Original')
plot(lenaR, 'Channel R')
plot(lenaG, 'Channel G')
plot(lenaB, 'Channel B')

plt.show()
