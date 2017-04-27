# telnet program example
import socket, select, string, sys

def prompt(user_name) :
    sys.stdout.write('\n')
    sys.stdout.write(' < '  + user_name +  ' > ')
    sys.stdout.flush()

#main function
if __name__ == "__main__":

    host = "localhost"
    port = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try :
        s.connect((host, port))
    except :
        print ("No se puede conectar")
        sys.exit()

    print ("Conectado!")
    data = s.recv(4096)
    print (data)
    user_name = raw_input("")
    s.send(user_name)
    prompt(user_name)

    while True:
        socket_list = [sys.stdin, s]

        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

        for sock in read_sockets:
            # Recibe los mensajes del servidor
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print ("Desconectado")
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    prompt(user_name)

            #user entered a message
            else :
                msg = sys.stdin.readline()
                s.send(msg)
                prompt(user_name)
