#!/usr/bin/python2
#
# This script reads from a file "linux.png" an image
# shows some images properties at command line and
# shows image on the screen
#

from scipy import misc
import matplotlib.pyplot as plt

# Read image from file
linuximage = misc.imread('../images/linux.png')

# Display on CMD some image properties
print "Image type: ", type(linuximage)
print "Image size: ",linuximage.size
print "Image shape: ",linuximage.shape
print "Image type: ", linuximage.dtype 

# Display image on the screen
plt.imshow(linuximage)
plt.show()
