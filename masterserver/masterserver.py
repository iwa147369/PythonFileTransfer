from header import *
from classClient import *
from classFileServer import *

def main():
    print("------------------------Master Server------------------------------")
    print("Ctrl C to exit.")
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.bind((MS_IP, MS_PORT))

    try:
        while True:
            tcpsock.listen(MAX_CONNECTION)
            print("Waiting connections ...\n")
            conn, (ip, port) = tcpsock.accept()        
            data = conn.recv(BUFFER_SIZE).decode("ascii")

            if data[:2] == "FS":
                addr = data[21:].split(":")
                print ("New file server connected: " + ip + ":" + str(port))
                newFileServerThread = FileServerThread(addr[0], addr[1], conn)
                newFileServerThread.start()
                threadsServer.append(newFileServerThread)
            elif data[:2] == "CL":
                print ("New client connected: " + ip + ":" + str(port))
                newClientThread = ClientThread(ip, port,conn)
                newClientThread.start()
                threadsClient.append(newClientThread)
    except Exception as e:
        pass

if __name__ == "__main__":
    main()

