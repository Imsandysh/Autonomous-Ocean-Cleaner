import socket
import sys
import cv2
import pickle
import numpy as np



vcap = cv2.VideoCapture("http://10.0.0.88:8160")

while(1):

    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)


# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# print ('Socket created')

# s.bind(("10.0.0.27",8080))
# print ('Socket bind complete')
# s.listen(10)
# print('Socket now listening')

# conn,addr=s.accept()

# while True:
#     data=conn.recv(80)
#     print (sys.getsizeof(data))
#     frame=pickle.loads(data)
#     print(frame)
#     cv2.imshow('frame',frame)

# rtsp_server = 'rtsp://10.0.0.88:8080'
# i = vlc.Instance("--vout=dummy --sout-mux-caching=<>")
# player = i.media_player_new()
# player.set_mrl(rtsp_server)
# player = vlc.MediaPlayer(rtsp_server)



# VIDEOWIDTH = 800
# VIDEOHEIGHT = 600

# # size in bytes when RV32
# size = VIDEOWIDTH * VIDEOHEIGHT * 4
# # allocate buffer
# buf = (ctypes.c_ubyte * size)()
# # get pointer to buffer
# buf_p = ctypes.cast(buf, ctypes.c_void_p)

# # global frame (or actually displayed frame) counter
# framenr = 0

# # vlc.CallbackDecorators.VideoLockCb is incorrect
# CorrectVideoLockCb = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))


# @CorrectVideoLockCb
# def _lockcb(opaque, planes):
#     print("lock", file=sys.stderr)
#     planes[0] = buf_p


# @vlc.CallbackDecorators.VideoDisplayCb
# def _display(opaque, picture):
#     print("display {}".format(framenr))
#     global framenr
#     if framenr % 24 == 0:
#         # shouldn't do this here! copy buffer fast and process in our own thread, or maybe cycle
#         # through a couple of buffers, passing one of them in _lockcb while we read from the other(s).
#         img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf, "raw", "BGRA", 0, 1)
#         img.save('img{}.png'.format(framenr))
#     framenr += 1


# vlc.libvlc_video_set_callbacks(pl, _lockcb, None, _display, None)
# player.video_set_format("RV32", VIDEOWIDTH, VIDEOHEIGHT, VIDEOWIDTH * 4)

# player.play()
