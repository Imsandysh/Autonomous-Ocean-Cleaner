from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import gpiozero
from gpiozero import Servo
from time import sleep

isClose = False
isCloseOld = False
myGPIO=17
 
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
servo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)
while True:
    servo.min()
    sleep(0.5)
    break


camera = PiCamera()
image_width = 640
image_height = 480
camera.resolution = (image_width, image_height)
camera.framerate = 32
rawCapture = PiRGBArray(camera,size = (image_width, image_height))
center_image_x = image_width/2
center_image_y = image_height/2
minimum_area = 3000
maximum_area = 100000

boat = gpiozero.Robot(left = (21,20), right = (23,24))
forward_speed= 1.0
turn_speed = 0.8

Val_Hue = 110

Col_low_Val = np.array([Val_Hue-10,100,100])
Col_Up_Val = np.array([Val_Hue+10,255,255])

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
 
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
 
    color_mask = cv2.inRange(hsv, Col_low_Val, Col_Up_Val)
 
    countours, hierarchy = cv2.findContours(color_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
 
    trash_area= 0
    trash_x = 0
    trash_y = 0
    for contour in countours:
        x, y, width, height = cv2.boundingRect(contour)
        found_area = width * height
        center_x = x + (width / 2)
        center_y = y + (height / 2)
        if trash_area < found_area:
            trash_area = found_area
            trash_x = center_x
            trash_y = center_y
    if trash_area > 0:
        trash_location = [trash_area, trash_x, trash_y]
    else:
        trash_location = None
 
    if trash_location:
        if (trash_location[0] > minimum_area) and (trash_location[0] < maximum_area):
            if trash_location[1] > (center_image_x + (image_width/3)):
                boat.right(turn_speed)
                print("Turning right")
            elif trash_location[1] < (center_image_x - (image_width/3)):
                boat.left(turn_speed)
                print("Turning left")
            else:
                boat.forward(forward_speed)
                print("Forward")
            isClose = False
        elif (trash_location[0] < minimum_area):
            boat.left(turn_speed)
            print("Target isn't large enough, searching")
            isClose = False
        else:

            if isClose == isCloseOld:
                boat.stop()
                print("Target large enough, stopping")
                while True:
                    servo.mid()
                    print("mid")
                    sleep(0.5)
                    servo.max()
                    print("max")
                    sleep(1)
                    break
                boat.left(forward_speed)
                sleep(0.5)
                boat.forward(forward_speed)
                sleep(3)
                while True:
                    servo.min()
                    sleep(0.5)
                    break
                isClose = True
                    
    else:

        boat.left(turn_speed)
        print("Target not found, searching")
 
    rawCapture.truncate(0)


