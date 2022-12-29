# Python File Transfer
<p>File Transfer - Python Networking </p>
<p> Authur: Iwa </p>

![alt](https://raw.githubusercontent.com/iwa147369/PythonFileTransfer/master/model_of_the_system.png?token=GHSAT0AAAAAAB4YLE6GDCHJTXDUDROTONMQY5NMHDQ)

# Introduction
The project consists of three main components: a master server, multiple file servers, and clients. The master server is responsible for maintaining information about the file servers and their shared files, while the file servers contain the actual files that can be shared with clients. Clients can connect to the master server and file servers to request the list of shared files and download them, respectively.

## Master Server
The master server has a fixed IP and port address and is responsible for the following tasks:

* Record the information sent by the file servers, including the list of shared files and the IP and port of the file server. This service uses the TCP protocol at the Transport layer.
* Provide a service for clients to retrieve the list of shared files, based on the IP and port of the file server. This service also uses the TCP protocol at the Transport layer.
* Allow multiple clients and file servers to connect at the same time.

## File Servers
The file servers contain the files that can be shared with clients. 

*When a file server starts up, it connects to the master server and sends its own information, including the list of shared files, IP address, and port, using the service provided by the master server (service #1). The file servers also provide the following service:

* A service for clients to download files, using the UDP protocol at the Transport layer. This service allows multiple clients to connect at the same time.
In addition, when a file server is down, the master server needs to remove the file list of the corresponding file server.

## Clients
Clients can use the following services provided by the master server and file servers:

* A service to retrieve the list of shared files from the master server, using the TCP protocol at the Transport layer.
* A service to download files from the file servers, using the UDP protocol at the Transport layer.
* Clients can also download multiple files at the same time.

## Protocol at the Application Layer
To ensure that the file is transferred reliably over the UDP protocol (service #3), a protocol has been designed at the Application layer to provide tree reliability. This ensures that the correct data of the file is reproduced.





