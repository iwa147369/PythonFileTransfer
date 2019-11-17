import socket
import os
import random
from classClient import *

FS_IP = "localhost"
FS_PORT = random.randint(10000,65535)

fileDir = "./File"

# ip, port of master server
MS_IP = "localhost"
MS_PORT = 1234

# The maximum amount of data to be received at once is specified by BUFFER_SIZE
BUFFER_SIZE = 1024

threads = []

def main():     
    print("------------------------File Server------------------------------")
    
    try:
        # Connect with MasterServer
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.connect((MS_IP, MS_PORT))
        tcpsock.send(("FS, Listen client at " + FS_IP + ":" + str(FS_PORT)).encode())
        tcpsock.recv(BUFFER_SIZE)
        
        # Send list file to MasterServer
        listFile = os.listdir(fileDir)
        listFile.append("end")
        for i in listFile:
            tcpsock.send(i.encode())
            tcpsock.recv(BUFFER_SIZE)

        # create UDP socket for client connected
        udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udpsock.bind((FS_IP, FS_PORT))
        while True:
            #recv file name and addr of client
            data, addr = udpsock.recvfrom(BUFFER_SIZE)
            print(data.decode("ascii"))
            newClient = ClientThread(addr, udpsock, data)
            newClient.start()
            threads.append(newClient)

        udpsock.close()
        tcpsock.close()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

   
