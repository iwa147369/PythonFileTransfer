from header import *

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        
    def run(self):
        listFile = ""

        #Send List file to client
        for thr in threadsServer:
            for i in thr.listFile:
                temp = i + ":" + thr.addr[0] + ":" + str(thr.addr[1]) 
                listFile += temp
                listFile += ";"
        
        if listFile != "":
            self.sock.send(listFile.encode()) 
        else:
            self.sock.send("empty".encode()) 
            
       