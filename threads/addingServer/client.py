import xmlrpclib

n = 100 # se puede poner cualquier numero
server = xmlrpclib.ServerProxy('http://localhost:8080/')
print ('adding number from 1 to ' ,n, " is equal to ", server.addThreads(n))
