from socket import error as socket_error
from config import buffer_size
from threading import Thread

class FileServer(Thread):

    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.addr = (ip, port)
        self.sock = sock
        self.files = []
        print("Connect with this file server at: " + self.addr[0] + ":" + str(self.addr[1]))        

    def run(self):
        # Recv List File from file server
        while True:
            self.sock.send("OK".encode())
            data = self.sock.recv(buffer_size).decode("ascii")
            if data == "end":
                break
            else:
                self.files.append(data)
                
        self.sock.send("OK".encode())
        try:
            data = self.sock.recv(buffer_size).decode("ascii")
        except socket_error as e:
            print(e)
            self.files = []
