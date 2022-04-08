from sendUDP import Message_manager

server = Message_manager("127.0.0.1",8080)

tuple2send = (5 ,3, 2, 1)

server.create_packet_send(tuple2send)