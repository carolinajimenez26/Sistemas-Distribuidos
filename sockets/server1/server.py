import socket

HOST = ''
PORT = 8080 # puerto por el que se establece la conexion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT)) # enlaza un socket a una direccion
s.listen(1) # maximo numero de conexiones encoladas
conn, addr = s.accept() # acepta la conexion,
print ('Connected by', addr) # muestra la direccion del socket (direccion IP + puerto)
print ('conn : ', conn) # nuevo socket, utilizado para enviar y recibir informacion en la conexion
while 1:
    data = conn.recv(1024)
    if not data: break
    print ("Client message: ", data)
    conn.sendall("Hello, I will serve you") # se envia un mensaje al cliente
conn.close() # se cierra la conexion
