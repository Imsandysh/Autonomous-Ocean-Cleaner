



class Message_manager():
   
    count
    def __init__(self,udp_ip,port = 8080):
        self.udp_ip = udp_ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        self.count = 0

    def dump(self,msg):
        self.sock.sendto(MESSAGE.encode(), (self.udp_ip, self.port))


    #x y width hieght
    def create_packet_send(self,tupleToSend):
        self.tupleToSend = tupleToSend
        self.count += 1
        self.tupleToSend.append(count)
        self.dump(self.tupleToSend)
