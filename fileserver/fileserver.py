import socket
import os

from client import Client
from config import *

def main():
    print("------------------------File Server------------------------------")
    
    try:
        # Connect with MasterServer
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_sock.connect((ms_ip, ms_port))
        tcp_sock.send(("FS, Listen client at " + fs_ip + ":" + str(fs_port)).encode())
        tcp_sock.recv(buffer_size)
        
        # Send list file to MasterServer
        list_file = os.listdir(file_dir)
        list_file.append("end")
        for i in list_file:
            tcp_sock.send(i.encode())
            tcp_sock.recv(buffer_size)

        # create UDP socket for client connected
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_sock.bind((fs_ip, fs_port))
        while True:
            # recv file name and addr of client
            data, addr = udp_sock.recvfrom(buffer_size)
            print(str(addr) + " download: " + data.decode("ascii"))
            new_client = Client(addr, udp_sock, data)
            new_client.start()
            threads.append(new_client)

        udp_sock.close()
        tcp_sock.close()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
