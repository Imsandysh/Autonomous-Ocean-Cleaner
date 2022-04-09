import numpy
import socket

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def receive_coords(TCP_IP, TCP_PORT):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6969
    s.connect(('192.168.137.206',port))
    print (s.recv(1024).decode())
    

TCP_IP = '192.168.137.206'
TCP_PORT = 6969
receive_coords(TCP_IP, TCP_PORT)
