import socket

HOST = 'localhost'
PORT = 8080 # puerto de conexion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crea objeto socket para enviar informacion
s.connect((HOST, PORT)) # se especifica la conexion
s.sendall('I am a client') # envia mensaje al servidor
data = s.recv(1024) # recibe infomracion del servidor
s.close() # se cierra la conexion
print 'Server message : ', repr(data)
