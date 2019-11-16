import socket
from threading import Thread
import os

BUFFER_SIZE = 1024

class ClientThread(Thread):

    def __init__(self,ip,port,sock, data):
        Thread.__init__(self)
        self.data = data.decode("ascii")
        self.ip = ip
        self.port = port
        self.sock = sock
        print ("New client connected: " + ip + ":" + str(port))
        self.run()

    def run(self):
        filename = "./File/" + self.data
        if (os.path.isfile(filename)):
            message= str(os.path.getsize(filename)) + ", download?(y/n)"
            self.sock.sendto(message.encode(), (self.ip,self.port))

            data, addr = self.sock.recvfrom(BUFFER_SIZE)
            if data.decode("ascii") == "y" or data.decode("ascii") == "Y":
                with open(filename, "rb") as f:
                    while True:
                        bytesToSend = f.read(BUFFER_SIZE)
                        if bytesToSend:
                            self.sock.sendto(bytesToSend, (self.ip,self.port))
                        else:
                            self.sock.sendto(b"", (self.ip,self.port))
                            print("Done.\n")
                            break
            else:
                print("ERR.")
        else:
            print("ERR.")
            self.sock.sendto("ERR".encode(), (self.ip,self.port))

