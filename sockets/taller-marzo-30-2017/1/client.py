import socket

HOST = 'localhost'
PORT = 8080 # puerto de conexion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crea objeto socket para enviar informacion
s.connect((HOST, PORT)) # se especifica la conexion

info = raw_input("Ingrese la base y el exponente: ")

s.sendall(info) # envia mensaje al servidor
data = s.recv(1024) # recibe infomracion del servidor
s.close() # se cierra la conexion
print 'Resultado: ', repr(data)
