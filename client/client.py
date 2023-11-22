import socket
import os
from threading import Thread

ms_ip = "localhost"
ms_port = 1234

buffer_size = 1024

class WorkerThread(Thread):
    def __init__(self, filename, udp_sock, addr):
        Thread.__init__(self)
        self.filename = filename
        self.udp_sock = udp_sock
        self.addr = addr
    
    def run(self):
        self.udp_sock.sendto(self.filename.encode(), self.addr)
        f = open(self.filename, "wb")
        while True:
            data, self.addr = self.udp_sock.recvfrom(buffer_size)
            if data != b"":
                f.write(data)
            else:
                f.close()
                break

def main():
    try:
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_sock.connect((ms_ip, ms_port))
        tcp_sock.send("CL".encode())

        data = tcp_sock.recv(buffer_size).decode("ascii")
        if data != "empty":
            list_file_data = data[:len(data) - 1].split(";")
            list_file = []
            print("List Files:")
            for i in range(0,len(list_file_data)):
                temp = list_file_data[i].split(":") 
                print(temp[0])
                list_file.append([temp[0], (temp[1], int(temp[2]))])

            udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            while True:
                filename = input("Download: ").split(" ")
                if filename[0] == "exit":
                    break
                for temp in filename:
                    for i in list_file:
                        if temp == i[0]:
                            addr = i[1]
                            break

                    new_thread = WorkerThread(temp, udp_sock, addr)
                    new_thread.start()

                print("Enter 'exit' to quit.")

            udp_sock.close()
        else:
            print("No files available for download.")
        tcp_sock.close()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
