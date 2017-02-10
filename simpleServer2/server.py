import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer as Server

class Operators:
    def add(self,a,b):
        return a + b
    def mult(self,a,b):
        return a * b
    def div(self,a,b):
        return a / b

port = 8080
server = Server(('localhost',port))
print ('Listening on port ', port)
server.register_instance(Operators())
server.serve_forever()
