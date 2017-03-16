import socket

s = socket.socket()
port = 8000
s.bind(("localhost", port))
s.listen(1)
print ("Server listening at port : " , port)
s.accept()

s.close()
