import socket, select

# Envia un mensaje a todos los sockets conectados menos a el mismo y al servidor
def broadcast_data (sock, message, clients, user_names):
    for socket in clients:
        if socket != s and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                clients.remove(socket)

# Busca el nombre de usuario de un socket determinado
def getUserName(user_names, sock):
    for name, client in user_names.items():
        if(client == sock):
            return name

    return None

# Elimina un socket de los usernames
def removeClient(user_names, sock):
    for name, client in user_names.items():
        if(client == sock):
            del user_names[name]

if __name__ == "__main__":

    clients = []
    user_names = dict()
    RECV_BUFFER = 4096
    PORT = 8080

    s = socket.socket()
    s.bind(('localhost', PORT))
    s.listen(5)

    clients.append(s)
    user_names["server"] = s

    print ("Servidor escuchando el puerto " , PORT)

    while True:
        read_sockets, write_sockets, error_sockets = select.select(clients,[],[]) # para esperar I/O

        for sock in read_sockets:
            if sock == s: # hay una nueva conexion
                new_client, addr = s.accept()
                clients.append(new_client)
                print ("Client (%s, %s) connected" % addr)

                while True:
                    new_client.send("Ingrese un nombre de usuario: ")
                    user_name = new_client.recv(1024)
                    print ("user_name : " + user_name)
                    if (user_name in user_names):
                        new_client.send("Nombre de usuario ya ha sido utilizado")
                    else:
                        user_names[user_name] = sock # agrega el nuevo miembro
                        new_client.send("Bienvenido al chat")
                        break

                msg = "Nuevo usuario: " + user_name
                broadcast_data(new_client, msg, clients, user_names) # avisa del nuevo miembro

            else: # recibe el mensaje del cliente
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        user_name = getUserName(user_names, sock)
                        if (not user_name):
                            sock.close()
                            clients.remove(sock)
                        else:
                            msg = "\r" + '<' + user_name + '> ' + data
                            broadcast_data(sock, msg, clients, user_names)

                except:
                    user_name = getUserName(user_names, sock)
                    if (not user_name):
                        sock.close()
                        clients.remove(sock)
                        removeClient(user_names, sock)
                    else:
                        msg = user_name + " se ha desconectado."
                        broadcast_data(sock, msg)
                        print (msg)
                        sock.close() # cierra la conexion con el socket
                        clients.remove(sock) # elimina el socket de la conexion
                        removeClient(user_names, sock) # elimina el nombre de usuario

    s.close()
