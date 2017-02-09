import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer as Server

def add(a,b):
    return a + b

port = 8080
connection = Server(('localhost',port))
print ('Listening on port ', port)
connection.register_function(add)
connection.serve_forever()
