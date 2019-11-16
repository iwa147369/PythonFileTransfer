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
    listFileData = data[:len(data) - 1].split(";")
    listFile = []
    print("List File:")
    for i in range(0,len(listFileData)):
        temp = listFileData[i].split(":") 
        print(temp[0])
        listFile.append([temp[0], (temp[1], int(temp[2]))])

    exitCode = 1
    while exitCode:
        filename = input("Download: ")

        addr = ()
        for i in listFile:
            if filename == i[0]:
                addr = i[1]
                break

        udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(addr)
        udpsock.sendto(filename.encode(), addr)
    
        # data, addr = udpsock.recvfrom(BUFFER_SIZE)
        # if data.decode("ascii") == "ERR":
        #     print("ERR")
        # elif data == "":
        #     print("Done.\n")
        # else:
        #     print(data.decode("ascii"))
        #     userReponse = input()
        #     udpsock.sendto(userReponse.encode(), (addr[0], int(addr[1])))
        #     if userReponse == "y" or userReponse == "Y":
        f = open(filename, "wb")
        while True:
            data, addr = udpsock.recvfrom(BUFFER_SIZE)
            if data != b"":
                f.write(data)
            else:
                f.close()
                print("Done.\n")
                break
            # else:
            #     pass
        exitCode = int(input("Press '0' to exit.\n"))
    udpsock.close()
    tcpsock.close()

if __name__ == "__main__":
    main()