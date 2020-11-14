import socket

url = input("Enter url- ")
url_sp = url.split('\')
HOST = url_sp[2]
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock = connect((HOST, PORT))
sd = "GET "+url+" HTTP/1.0\r\n\r\n".encode()
#sd = b'GET '+url+' HTTP/1.0\r\n\r\n'
mysock.sendall(sd)

doc = b"" #creates an empty byte variable
while True:
    data = mysock.recv(512)
    if len(data) < 1:   break
    doc += data

# To find the end of the header
dets = doc.find('\r\n\r\n'.encode())
#dets = doc.find(b'\r\n\r\n')
print(data[dets+1:].decode()) #this skips the header data
