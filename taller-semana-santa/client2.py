import socket

HOST = 'localhost'
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall("Client2")
data = s.recv(1024)
print ("Respuesta del servidor: ",data)
s.close()
