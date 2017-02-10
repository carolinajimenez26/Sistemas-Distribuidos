import xmlrpclib

a = 3
b = 5
client = xmlrpclib.ServerProxy('http://localhost:8080/')
print ('add : ', client.add(a,b))
print ('mult : ', client.mult(a,b))
print ('div : ', client.div(a,b))
