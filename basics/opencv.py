#!/usr/bin/python2
#
# Link https://www.hdm-stuttgart.de/~maucher/Python/ComputerVision/html/basicOperations.html
import cv2
#file="/home/lucifer/video.mp4"
file="/home/lucifer/videocam.webm"
cam = cv2.VideoCapture(file)

print "Video Properties:"
print "\t Width: ",cam.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
print "\t Height: ",cam.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
print "\t FourCC: ",cam.get(cv2.cv.CV_CAP_PROP_FOURCC)
print "\t Framerate: ",cam.get(cv2.cv.CV_CAP_PROP_FPS)
print "\t Number of Frames: ",cam.get(7)

while True:
        img2 = cam.read()[1]
        # Split RGB Channels
        b,g,r = cv2.split(img2)
        # Inversion of Channel R
        r=255-r
        # To join again channels
        # img = cv2.merge((b,g,r))
        cv2.imshow("Video",r)
        if cv2.waitKey(1) == 27:
                break

cam.release()
