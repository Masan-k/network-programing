# echo-client.py

import socket
import time
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
      message = input()
      s.sendall(message.encode())
      data = s.recv(1024)
      print("Received ", repr(data))
      if data.decode() == 'end':
        print("input end ...exit")
        break
