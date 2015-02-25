USAGE = """

This program records and displays video feed from a USB camera

Usage:
python cam.py
python cam.py "camera number"
python cam.py "camera number" "output file basename"

Example:
python cam.py 1 underwaterCam

"""

from time import localtime, strftime
import time
import numpy as np
import cv2
import sys

# Get command line arguments
print USAGE
if len(sys.argv) <= 1:
    cameraNum = 0
    basename = "camera"
elif len(sys.argv) == 2:
    cameraNum = int(sys.argv[1])
    basename = "camera"
elif len(sys.argv) == 3:
    cameraNum = int(sys.argv[1])
    basename = str(sys.argv[2])
    
# Create video capture object
cap = cv2.VideoCapture(cameraNum)

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
wd = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
ht = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
fps = int(14)
outputFileName = basename + '_' + strftime('%Y%m%d_%H %M %S', localtime())
out = cv2.VideoWriter(outputFileName + '.avi',fourcc, fps, (wd,ht), True)

# Start time
t = time.clock() # starts at zero when the program starts

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Finish waiting for 40ms before continuing to record and display frame
    d=0
    while (time.clock() - t < 1.0/fps):
        d=d+1
    t = time.clock()

    # Write frame to file
    out.write(frame)

    # Display  frame
    cv2.imshow(outputFileName,frame)
    
    # Quit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()