from threading import Thread
from config import threads_server

class Client(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        
    def run(self):
        files = ""

        #Send List file to client
        for thr in threads_server:
            for i in thr.files:
                temp = i + ":" + thr.addr[0] + ":" + str(thr.addr[1]) 
                files += temp
                files += ";"
        
        if files != "":
            self.sock.send(files.encode()) 
        else:
            self.sock.send("empty".encode()) 
            
       