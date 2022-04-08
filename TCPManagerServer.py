import socket
import threading

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)



class tcpManager:

    
    def __init__(self,HOST, PORT = 8080):
        self.HOST = HOST
        self.PORT = PORT
        self.s.bind((HOST, PORT))
        self.t1 = threading.Thread(target =start_server )
        

        #self.t1.join()
        

        def start_server(self):
            s.listen()
            conn, addr = s.accept()
            with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

        def kill(self):
            self.t1.join()
            self.t1.close()