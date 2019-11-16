import socket
from threading import Thread
import os

BUFFER_SIZE = 1024

class ClientThread(Thread):

    def __init__(self,addr,sock, data):
        Thread.__init__(self)
        self.data = data.decode("ascii")
        self.addr = addr
        self.sock = sock
        print ("New client connected: " + self.addr[0] + ":" + str(self.addr[1]))
        # self.run()

    def run(self):
        filename = "./File/" + self.data
        if (os.path.isfile(filename)):
            with open(filename, "rb") as f:
                while True:
                    bytesToSend = f.read(BUFFER_SIZE)
                    if bytesToSend:
                        self.sock.sendto(bytesToSend, self.addr)
                    else:
                        self.sock.sendto(b"", self.addr)
                        break
        else:
            print("ERR.")
            self.sock.sendto("ERR".encode(), self.addr)

