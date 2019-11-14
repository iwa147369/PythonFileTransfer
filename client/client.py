import socket
import os

MS_IP = "localhost"
MS_PORT = 1234

BUFFER_SIZE = 1024

def main():
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.connect((MS_IP, MS_PORT))
    tcpsock.send("CL".encode())

    data = tcpsock.recv(BUFFER_SIZE).decode("ascii")
    listFile = data.split(":")
    print("List File:")
    for i in listFile:
        print(i)
        
    exitCode = 1
    while exitCode:
        filename = input("Download: ")
        tcpsock.send(filename.encode())
        data = tcpsock.recv(BUFFER_SIZE).decode("ascii")
        addr = data.split(":")

        udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udpsock.sendto(filename.encode(), (addr[0], int(addr[1])))
    
        data, addr = udpsock.recvfrom(BUFFER_SIZE)
        if data.decode("ascii") == "ERR":
            print("ERR")
        elif data == "":
            print("Done.\n")
        else:
            print(data.decode("ascii"))
            userReponse = input()
            udpsock.sendto(userReponse.encode(), (addr[0], int(addr[1])))
            if userReponse == "y" or userReponse == "Y":
                f = open(filename, "wb")
                while True:
                    data, addr = udpsock.recvfrom(BUFFER_SIZE)
                    if data != b"":
                        f.write(data)
                    #print(data)
                    #print("\n")
                    else:
                        f.close()
                        udpsock.close()
                        print("Done.\n")
                        break
            else:
                pass
        exitCode = int(input("Press '0' to exit.\n"))
        
    tcpsock.close()

if __name__ == "__main__":
    main()