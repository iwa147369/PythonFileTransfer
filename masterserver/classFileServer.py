from header import *

class FileServerThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        self.listFile= []
        print("Connect with this file server at: " + self.ip + ":" + self.port)        
        self.run()

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
        # data = self.sock.recv(BUFFER_SIZE).decode("ascii")


