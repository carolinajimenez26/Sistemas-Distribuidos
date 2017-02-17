"""cuando se lanza el cliente debe presentar el siguiente menu:

##############BIENVENIDOS AL MENU ARITMETICO#####################"
				1. POTENCIA"
				2. FACTORIAL"
				3. SERIE DE FIBONACCI"
				4. LLENAR LISTA/TUPLA"
				0. SALIR"
en la opcion 1 se debe leer dos parametros e invocar la RPC del servidor
en la opcion 2 se debe leer 1 parametro e invocar la RPC  del servidor.
en la opcion 3 se debe leer 1 parametro e invocar la RPC del servidor.
en la opcion 4 se debe llenar una lista o tupla por teclado, guardar
en un archivo de texto en invocar la RPC  del servidor con ese archivo como parametro."""

import xmlrpclib
import os
import math

def make_file(data):
    file_name = "data.txt"
    file = open(file_name,'w+') # creates the file
    i = 0
    for item in data:
        if (i != 0):
            file.write("\n" + str(item))
        else:
            file.write(str(item))
        i += 1
    file.close()
    return file_name

def menu():
	print "##############BIENVENIDOS AL MENU ARITMETICO#####################"
	print "			1. POTENCIA"
	print "			2. FACTORIAL"
	print "			3. SERIE DE FIBONACCI"
	print "			4. LLENAR LISTA/TUPLA"
	print "			Cualquier otro para SALIR"

def conectar():
	menu()
	a = input('Ingrese una opcion: ')
	if a == 1:
		os.system('clear')
		b = input('Ingrese la base: ')
		c = input('Ingrese el exponente: ')
		print "El valor de la potencia es : "+str(proxy.potencia(b,c))

	elif a == 2:
		os.system('clear')
		n=input("ingrese un entero: ")
		print "el factorial de : "+str(n)+str(" es: ")+str(proxy.factorial(n))

	elif a == 3:
		os.system('clear')
		n = input("ingrese un entero: ")
		print "el numero de fibonacci es: "+str(proxy.fibonacci(n))

	elif a == 4:
		os.system('clear')
		l = raw_input("ingrese los numeros con espacios: ")
		l = l.rstrip().split(" ") # quita espacios y lo pone en una lista como strings
		file_name = make_file(l) # lo inserta en un documento de texto
		# envia el archivo de texto
		with open("client" + file_name, "wb") as handle:
		    handle.write(proxy.receive_data(file_name).data) # no se sabe cuando termina de enviar

		proxy.get_data()

	else :
		print "para el servidor y todo el equipo fue un placer atenderle, regresa pronto a nuestro MENU"
		exit()

proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
conectar()
