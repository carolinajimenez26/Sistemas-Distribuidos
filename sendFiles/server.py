from SimpleXMLRPCServer import SimpleXMLRPCServer as Server
import xmlrpclib

# recibe el archivo de texto
def receive_data(file_name):
     with open(file_name, "rb") as handle:
         return xmlrpclib.Binary(handle.read())

def get_file(file_name):
    file = open(file_name,'r')
    data = []
    for item in file:
        data.append(int(item.rstrip()))
    file.close()
    return data

port = 8000
server = Server(("localhost", port))
print ("Listening on port ", port)
server.register_function(receive_data)
a = get_file("clientdata.txt") # pasa datos de archivo a una variable
print ("receive: ", a)

server.serve_forever()
