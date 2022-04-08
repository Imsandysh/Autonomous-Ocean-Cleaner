

import socket


class Message_manager():
   
    def __init__(self,udp_ip,port = 8080):
        self.udp_ip = udp_ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.count = 0

    def dump(self,msg):
        if isinstance(msg ,str ):
            self.sock.sendto(bytes(msg, "utf-8"), (self.udp_ip, self.port))
        else:
            self.sock.sendto(msg, (self.udp_ip, self.port))

    #x y width hieght frame
    def create_packet_send(self,tupleToSend):
        tupleToSend
        temp = list(tupleToSend)
        self.count += 1
        temp.append(self.count)
        self.tupleToSend = tuple(temp)
        res = self.convertTuple(self.tupleToSend)
        self.dump(res)

    def convertTuple(self,tup):
        temp = list(tup)
        str_make = " ".join(str(x) for x in temp)
        return str_make
