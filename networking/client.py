import socket

s = socket.socket()

port = 6969

s.connect(('192.168.137.206', port))

print (s.recv(1024).decode())

s.close()