import socket

HOST = 'localhost'
PORT = 8080
clients_number = 0

while (True): # crea clientes
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall("Client"+str(clients_number))
    data = s.recv(1024)
    print ("Respuesta del servidor: ",data)
    clients_number += 1
    s.close()
