from SimpleXMLRPCServer import SimpleXMLRPCServer as Server
import xmlrpclib

def python_logo():
     with open("python_logo.png", "rb") as handle:
         return xmlrpclib.Binary(handle.read())

port = 8000
server = Server(("localhost", port))
print ("Listening on port ", port)
server.register_function(python_logo)

server.serve_forever()
