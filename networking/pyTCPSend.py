
from turtle import shape
from typing import final
import cv2
import numpy as np
import socket
import sys
import pickle
import time
from PIL import Image

# from picamera.array import PiRGBArray
# from picamera import PiCamera

#import gpiozero

#setup
# camera = PiCamera()
# image_width = 640
# image_height = 480
# camera.resolution = (image_width, image_height)
# camera.framerate = 32
# rawCapture = PiRGBArray(camera,size = (image_width, image_height))


HOST = '192.168.137.206'
PORT = 8081

print("start")



# def take_picture_upload():
#     time.sleep(0.1)
#     camera.capture(rawCapture, format="bgr")
#     image = rawCapture.array
#     encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
#     result, imgencode = cv2.imencode('.jpg', image, encode_param)
#     data = numpy.array(imgencode)
#     stringData = data.tostring()

#     sock.send( str(len(stringData)).ljust(16));
#     sock.send( stringData );
#     sock.close()

def windows_take_picture_upload():
    
    try:
        s = socket.socket()
        s.connect((HOST, PORT))
        print ("Socket created and connected")
        #cam = cv2.VideoCapture(0)
        
        #ret,frame = cam.read()
        #cv2.imshow('img1',frame)
        # res = cv2.waitKey(0)
        # encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
        # result, imgencode = cv2.imencode('.jpg', frame, encode_param)


        image =  Image.open("crumpled-paper.webp").convert('RGB')
        w, h = image.size
        
        data = np.array(image.getdata()).reshape((h,w,3)).astype(np.uint8)
        shape = " ".join(map(str, (h,w,3)))
        stringData = data.tobytes()
        length = len(stringData)
        
        s.send(str(length).ljust(16).encode())
        s.send(shape.ljust(16).encode())
        s.send(stringData)

        print ("receiving bbox coordinates...")
        coords = s.recv(1024).decode()
        print (coords)

    except Exception as e:
        print (e)
    except KeyboardInterrupt as e:
        print (e)
    except:
        print (sys.exc_info())
    finally:
        print ("closing socket...")
        s.close()



windows_take_picture_upload()