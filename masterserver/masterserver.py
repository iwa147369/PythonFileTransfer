import socket

from client import Client
from file_server import FileServer
from config import ms_ip, ms_port, buffer_size, threads_client, threads_server, MAX_CONNECTION

def main():
    print("------------------------Master Server------------------------------")
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.bind((ms_ip, ms_port))

    try:
        while True:
            tcp_sock.listen(MAX_CONNECTION)
            print("Waiting connections ...\n")
            conn, (ip, port) = tcp_sock.accept()        
            data = conn.recv(buffer_size).decode("ascii")

            if data[:2] == "FS":
                addr = data[21:].split(":")
                print("New file server connected: " + ip + ":" + str(port))
                new_file_server_thread = FileServer(addr[0], addr[1], conn)
                new_file_server_thread.start()
                threads_server.append(new_file_server_thread)
            elif data[:2] == "CL":
                print("New client connected: " + ip + ":" + str(port))
                new_client_thread = Client(ip, port, conn)
                new_client_thread.start()
                threads_client.append(new_client_thread)
    except Exception as e:
        pass

if __name__ == "__main__":
    main()
