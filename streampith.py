import cv2

vcap = cv2.VideoCapture("http://10.0.0.88:8160")

while(1):

    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)