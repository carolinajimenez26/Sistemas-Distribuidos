import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer as Server

class Operaciones:
	#### servicios
	def potencia(self,x,y):
		if y==0:
			return 1
		else:
			return self.potencia(x,y-1)*x
	def factorial(self,n):
		if n==0:
			return 1
		else:
			return self.factorial(n-1)*n
	def fibonacci(self,n):
		if n==0:
			return 0
		elif n==1:
			return 1
		else:
			return self.fibonacci(n-1)+self.fibonacci(n-2)

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

conexion = Server(('localhost',8000))
print "###################servidor ONLINE #####################################"
print "Soy el servidor y estoy escuchando por el puerto:" + str(8000)
conexion.register_instance(Operaciones())
conexion.serve_forever()
