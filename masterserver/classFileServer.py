from header import *

class FileServerThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.addr = (ip, port)
        self.sock = sock
        self.listFile= []
        print("Connect with this file server at: " + self.addr[0] + ":" + str(self.addr[1]))        

    def run(self):
        # Recv List File from file server
        while True:
            self.sock.send("OK".encode())
            data = self.sock.recv(BUFFER_SIZE).decode("ascii")
            if data == "end":
                break
            else:
                self.listFile.append(data)
                
        self.sock.send("OK".encode())
        try:
            data = self.sock.recv(BUFFER_SIZE).decode("ascii")
        except socket.error as e:
            print(e)
            self.listFile = []



