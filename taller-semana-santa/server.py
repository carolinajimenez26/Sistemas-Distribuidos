import socket
import thread

def on_new_client(clientsocket,addr,tid):
    while (True): # escucha al cliente siempre que no se haya cerrado la conexion
        msg = clientsocket.recv(1024) # recibe el mensaje del cliente
        print ("Mensaje del cliente: ", msg)
        msg = "Hola, eres el cliente numero " + str(tid)
        clientsocket.send(msg) # envia el mensaje al cliente
    clientsocket.close() # termina la conexion con el cliente

s = socket.socket()
port = 8080

print ("Servidor escuchando el puerto " , port)

s.bind(('localhost', port))
s.listen(5)
clients_number = 0

while (True): # clientes indefinidos
   c, addr = s.accept()     # Establece conexion con el cliente
   thread.start_new_thread(on_new_client,(c,addr,clients_number)) # nuevo hilo para cada cliente
   clients_number += 1
s.close() # termina la conexion
