import socket
import thread

def on_new_client(clientsocket,addr,clients):
    msg = clientsocket.recv(1024) # recibe el primer mensaje del cliente
    print ("Mensaje del cliente: ", msg)
    msg = "Ingrese un nombre de usuario "
    clientsocket.send(msg)
    user_name = clientsocket.recv(1024)
    print ("Usuario: ", user)
    clients.append((user_name,clientsocket)) # agrega a la lista el nuevo cliente
    while (True): # sigue escuchando al cliente
        msg = clientsocket.recv(1024) # recibe el mensaje del cliente
        print ("Mensaje del cliente: ", msg)

        for i in range (0,len(clients)): # envia el mensaje a los otros usuarios
            user = clients[i]
            if (user[0] != user_name): # no se envia el mensaje a si mismo
                user[1].send(msg)

    clientsocket.close() # termina la conexion con el cliente

s = socket.socket()
port = 8080

print ("Servidor escuchando el puerto " , port)

s.bind(('localhost', port))
s.listen(5)
clients = []

while (True): # clientes indefinidos
   c, addr = s.accept()     # Establece conexion con el cliente
   thread.start_new_thread(on_new_client,(c,addr,clients)) # nuevo hilo para cada cliente
   print "number of clients: " + str(len(clients))
s.close() # termina la conexion
