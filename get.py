# HTTPClient used to process GET / POST Requests
import logging
import socket
import sys


s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     

s.connect(('www.cnn.com', 80))
s.sendall("GET / HTTP/1.1\r\nHost: www.cnn.com\r\nContent-Type: application/json\r\n\r\n")

print(s.recv(4096))
s.close