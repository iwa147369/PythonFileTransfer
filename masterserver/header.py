import socket
from threading import Thread

MAX_CONNECTION = 5

MS_IP = "localhost"
MS_PORT = 1234
BUFFER_SIZE = 1024

threadsServer = []
threadsClient = []
