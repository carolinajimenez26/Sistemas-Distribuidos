import socket, select

def broadcast_data (sock, message, clients, user_names):
    for socket in clients:
        if socket != s and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                clients.remove(socket)

if __name__ == "__main__":

    clients = []
    user_names = dict()
    RECV_BUFFER = 4096
    PORT = 8080

    s = socket.socket()
    s.bind(('localhost', PORT))
    s.listen(5)

    # Add server socket to the list of readable connections
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
                msg = "[%s:%s] entered room\n" % addr
                broadcast_data(new_client, msg, clients, user_names)

            else: # recibe el mensaje del cliente
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        msg = "\r" + '<' + str(sock.getpeername()) + '> ' + data
                        broadcast_data(sock, msg, clients, user_names)

                except:
                    msg = "Client (%s, %s) is offline" % addr
                    broadcast_data(sock, msg)
                    print (msg)
                    sock.close() # cierra la conexion con el socket
                    clients.remove(sock) # elimina el socket de la conexion
                    continue

    s.close()
