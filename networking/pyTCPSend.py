
import cv2
import numpy as np
import socket
import sys
import pickle

from picamera.array import PiRGBArray
from picamera import PiCamera

import gpiozero

#setup
camera = PiCamera()
image_width = 640
image_height = 480
camera.resolution = (image_width, image_height)
camera.framerate = 32
rawCapture = PiRGBArray(camera,size = (image_width, image_height))


TCP_IP = '10.0.0.242'
TCP_PORT = 6969

sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))



def take_picture_upload():
    time.sleep(0.1)
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    result, imgencode = cv2.imencode('.jpg', image, encode_param)
    data = numpy.array(imgencode)
    stringData = data.tostring()

    sock.send( str(len(stringData)).ljust(16));
    sock.send( stringData );
    sock.close()

def windows_take_picture_upload():
    cam = cv2.VideoCapture(0)
    ret,frame = cam.read()
    time.sleep(0.1)
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    data = numpy.array(imgencode)
    stringData = data.tostring()

    sock.send( str(len(stringData)).ljust(16));
    sock.send( stringData );
    sock.close()



