import socket
import sys

def authentication(user, password):
    user_admin = 'german'
    password_admin = '1234'
    if user == user_admin and password == password_admin:
        return 'True'
    else:
        return 'False'

#Se crea una instancia del socket, al usar SOCK_STREAM se utiliza el protocolo TCP/IP
Mi_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#El metodo bind() configura la direccion IP y el puerto que se va a utilizar
Mi_socket.bind(("localhost", 8000))
#El metodo listen() pone al socket en modo servidor, el parametro indica la cantidad de clientes que puede recibir
Mi_socket.listen(5)
while True:
    # Esperando conexion
    print 'Esperando clientes'
    #El metodo accept() permite y acepta una conexion entrante ademas de la direccion del cliente
    connection, client_address = Mi_socket.accept()

    try:
        print 'concexion desde', client_address

        # Recibe los datos en trozos y reetransmite
        while True:
            #El metodo recv() lee la conexion entrante, el parametro indica la cantidad de datos que recibira
            data = connection.recv(100)
            if data:
                print '* Mensaje recibido '
                print data
                user, password = data.split()
                login = authentication(user, password)
                #El metodo sendall() permite transmitir los datos al cliente
                # newdata='Mensaje recibido, respuesta desde servidor'
                print '* Enviando respuesta'
                connection.sendall(login)
            else:
                print 'no hay mas datos', client_address
                break

    finally:
        # Cerrando conexion
        connection.close()
