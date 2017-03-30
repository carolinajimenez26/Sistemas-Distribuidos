import socket
import sys
import getpass

# Se crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta el socket en el puerto cuando el servidor este escuchando
server_address = ('localhost', 8000)
#print 'conectando a %s puerto %s' % server_address
#El metodo connect permite establecer conexion del socket en el puerto e IP establecida
sock.connect(server_address)

try:
    user = raw_input('Ingrese nombre de usuario: ')
    #getpass oculta la escritura de contrasena
    password = getpass.getpass()
    print password
    data = user + " " + password

    # Enviando datos
    #message = 'Soy el cliente, solicito respuesta'

    print '* buscando usuario: "%s"' % user
    sock.sendall(data)

    # Buscando respuesta
    amount_received = 0
    amount_expected = len(data)

    while amount_received < amount_expected:
        #El metodo recv() lee la conexion entrante, el parametro indica la cantidad de datos que recibira
        data = sock.recv(100)
        amount_received += len(data)

        if data == 'True':
            print 'Hola %s, Bienvenido al servidor' %user
        else:
            print "Datos incorrectos, verifique usuario y contrasena"

        break
        #print >>sys.stderr, '* recibiendo "%s"' % data

finally:
    print >>sys.stderr, 'cerrando socket'
    #Cierra conexion del socket
    sock.close()
