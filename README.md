This repo is used to share/collaborate Python code based on assigments in  Coursera Course 


Fundamentals of Digital Image and Video Processing
by Aggelos K. Katsaggelos

I am not a developer, I made this only for fun. After searching I found that the most interesting libraries to use will be NumPy and SciPy.
Here are some interesting links to begin:

* http://scipy-lectures.github.io/advanced/image_processing/
* https://atoms.scilab.org/categories/image_processing
* http://scikit-image.org/

##List of Scripts

- basics/readImage.py           Reads image from a file and displays it on screen
- basics/displayImage.py        Displays an image and save it to a file
- basics/basicManipulation.py   Basic pixel manipulation
- basics/infoImage.py           Shows image statistics and plots histogram
- basics/colorImage.py          Extract RGB image channels and displays them
- basics/denoiseImage.py	Add noise to Lena image and remove it with predefined Gaussian and Median filters
- basics/geometricTrans.py	Basic geometrical transformations
- basics/opencv.py		Open a video file, got one RGB channel and invert it
- basics/opencv-webcam-detection.py Open webcam device and apply detection algo to detect face and eyes, depending passed parameter
- basics/opencv-histogramEq.py  Plot image histogram
- basics/opencv-histogram.py    Plot image histogram
- basics/haarcascade_eye.xml    XML files for EYE opencv detection
- basics/haarcascade_frontalface_default.xml	XML files for EYE opencv detection
- filters/low-pass.py		Resolution of problem 7 assigment 1
- filters/rescale.py            Resolution of problem 8 assigment 2, PSNR not equal that got in Matlab!


##Installation

### Arch Linux
Archlinux up to date + Python 2.7.9 + Python2 Scipy + Python2 PIL + Python2 NumPy + IPython2

```sh
$sudo pacman -S python2-scipy python2-pillow python2-matplotlib python2-numpy
```

### Debian / Ubuntu / Mint
```sh
$sudo apt-get install python python-scipy python-pil python-matplotlib python-numpy
```

