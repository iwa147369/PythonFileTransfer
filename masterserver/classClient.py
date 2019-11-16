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
        for thr in threadsServer:
            for i in thr.listFile:
                temp = i + ":" + thr.ip + ":" + thr.port 
                listFile += temp
                listFile += ";"
        self.sock.send(listFile.encode()) 

        # data = self.sock.recv(BUFFER_SIZE).decode("ascii")
        # for thr in threadsServer:
        #     for i in thr.listFile:
        #         if (data == i):
        #             self.sock.send((thr.ip + ":" + str(thr.port)).encode())
        #             break

