import socket

HOST = 'localhost'
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
msgs = ["¡Hola!", "¿Que mas?", "Bien :)"]
idx = 0

while True:
    s.sendall(msgs[i%len(msgs)])
    i += 1
    data = s.recv(1024)
    print ("Respuesta del servidor: ",data)
s.close()
