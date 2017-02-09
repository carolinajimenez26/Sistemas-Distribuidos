import xmlrpclib

a = 3
b = 5
proxy = xmlrpclib.ServerProxy('http://localhost:8080/')
print ('adding : ',proxy.add(a,b))
