import socket

def potencia(base,exp):
    suma = 1
    for i in range(0,exp):
        suma *= base
    return suma

HOST = ""
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1) # maximo numero de conexiones encoladas
conn, addr = s.accept() # acepta la conexion,
print ('Connected by', addr)
print ('conn : ', conn)
while 1:
    data = conn.recv(1024)
    if not data: break
    base, exp = data.split()
    print (data)
    print ("Base: ", base)
    print ("Exponente: ", exp)
    ans = potencia(int(base),int(exp))
    conn.sendall(str(ans))
conn.close() # se cierra la conexion
