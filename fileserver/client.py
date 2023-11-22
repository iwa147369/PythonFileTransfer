import socket
import os
from threading import Thread
from config import buffer_size

class Client(Thread):

    def __init__(self, addr, sock, data):
        Thread.__init__(self)
        self.data = data.decode("ascii")
        self.addr = addr
        self.sock = sock
        print("New client connected: " + self.addr[0] + ":" + str(self.addr[1]))

    def run(self):
        file_path = "./File/" + self.data
        if os.path.isfile(file_path):
            with open(file_path, "rb") as f:
                while True:
                    bytes_to_send = f.read(buffer_size)
                    if bytes_to_send:
                        self.sock.sendto(bytes_to_send, self.addr)
                    else:
                        self.sock.sendto(b"", self.addr)
                        break
        else:
            print("ERR.")
            self.sock.sendto("ERR".encode(), self.addr)
