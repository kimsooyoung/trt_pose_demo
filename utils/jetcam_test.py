import cv2
from jetcam.usb_camera import USBCamera
import numpy as np
import matplotlib.pyplot as plt

camera = USBCamera(capture_device=0)
camera.running = True

def callback(change):
    new_image = change['new']
    cv2.imshow('image', new_image)
    cv2.waitKey(0)
    # do some processing...

while cv2.waitKey(33) < 0:
    image = camera.value
    cv2.imshow("VideoFrame", image)

cv2.destroyAllWindows()
