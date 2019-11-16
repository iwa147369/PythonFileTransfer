from header import *

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        
        self.run()

    def run(self):
        listFile = ""

        #Send List file to client
        for thr in threadsServer:
            for i in thr.listFile:
                temp = i + ":" + thr.addr[0] + ":" + str(thr.addr[1]) 
                listFile += temp
                listFile += ";"
        self.sock.send(listFile.encode()) 

       