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
    print("invalid email address")

count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:   break
    count += len(data)
    if count <= 3000:
        print(data.decode(), end='')
print("Overall number of characters in the document is",count)


mysock.close()
