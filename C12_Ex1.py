import socket

try:
    URL = input("Enter URL - ")

    url_sp = URL.split('/')
    HOST = url_sp[2]
    PORT = 80
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((HOST, PORT))
    cmd = 'GET '+URL+' HTTP/1.0\r\n\r\n'.encode()
#cmd = b'GET '+URL+' HTTP/1.0\r\n\r\n'
    mysock.send(cmd)
except:
    print(" Invalid URL")

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
