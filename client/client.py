import socket
import os
from threading import Thread

MS_IP = "localhost"
MS_PORT = 1234

BUFFER_SIZE = 1024

class WorkerThread(Thread):
    def __init__(self, filename, udpsock, addr):
        super().__init__()
        self.filename = filename
        self.udpsock = udpsock
        self.addr = addr
        self.DownloadFileFromFileServer()
    
    def DownloadFileFromFileServer(self):
        self.udpsock.sendto(self.filename.encode(), self.addr)
        f = open(self.filename, "wb")
        while True:
            data, self.addr = self.udpsock.recvfrom(BUFFER_SIZE)
            if data != b"":
                f.write(data)
            else:
                f.close()
                print("Done.\n")
                break

def main():
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.connect((MS_IP, MS_PORT))
    tcpsock.send("CL".encode())

    data = tcpsock.recv(BUFFER_SIZE).decode("ascii")
    listFileData = data[:len(data) - 1].split(";")
    listFile = []
    print("List File:")
    for i in range(0,len(listFileData)):
        temp = listFileData[i].split(":") 
        print(temp[0])
        listFile.append([temp[0], (temp[1], int(temp[2]))])

    try:
        while True:
            filename = input("Download: ")

            addr = ()
            for i in listFile:
                if filename == i[0]:
                    addr = i[1]
                    break

            udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            newThread = WorkerThread(filename, udpsock, addr)
            newThread.start()

            print("Ctrl C to exit.")
    except Exception as e:
        print(e)

    udpsock.close()
    tcpsock.close()

if __name__ == "__main__":
    main()