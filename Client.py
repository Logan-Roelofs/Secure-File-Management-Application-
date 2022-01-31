#!/usr/bin/python2
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1",54321))
print("Connection Established To Server")
while True:
        message = sock.recv(1024)
        print (message)
        if message == "q":
                break  
        else:
                message_back = raw_input("Type Message To Send To Server: ")
                sock.send(message_back)
sock.close()