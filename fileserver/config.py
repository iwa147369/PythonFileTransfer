import random

fs_ip = "localhost"
fs_port = random.randint(10000, 65535)

file_dir = "./File"

# ip, port of master server
ms_ip = "localhost"
ms_port = 1234

# The maximum amount of data to be received at once is specified by BUFFER_SIZE
buffer_size = 1024

threads = []