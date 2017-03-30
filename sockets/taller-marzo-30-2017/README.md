Para la clase de hoy en la segunda hora se requiere lo siguiente(Grupos de dos estudiantes):

1. Crear un programa cliente y un programa servidor.

  1. Establecer un socket de conexión entre ellos.

  2. Cuando se lanza el cliente, se debe solicitar un dato numérico por teclado.

  3. Se debe enviar dicho dato al servidor via socket.

  4. En el lado del servidor se debe implementar potencia()

  5. Se debe instanciar potencia() con el dato recibido del cliente

  6. Via socket se debe enviar el resultado de invocar portencia()

  7. Se debe imprimir en el cliente dicho resultado.

2. Implementar un cliente y un servidor.

  1. Establecer un socket de conexion entre ellos.

  2. En el lado del servidor debe existir una función similar a :

```python
def autenticacion(loggin, passw):
     log='cesar_jaramillo_distribuidos'
     passwd: '123456789'
```

  3. cuando se lanza el cliente se le debe solicitar loggin y password(enmascarar) los cuales serán enviados al servidor via socket.

  4. Se debe ejecutar la función autenticacion() con los parametros enviados por el cliente, se debe tomar las siguientes determinaciones:

    - si los datos enviados por el cliente, coinciden con las variables en la función, se debe enviar el siguiente mensaje al cliente: _Hola Cesar, Bienvenido al servidor_.

    - si no coinciden se debe enviar el mensaje: _Lamentamos informarte que los datos de autenticación no coinciden_"

  5. Cerrar la conexión

### Ejemplo autenticación:

```python
def autenticacion(loggin, passw):
	logg='cesar_jaramillo_distribuidos'
	passwd='123456789'
	if logg==loggin and passwd==passw:
		return True
	else:
		return False

print autenticacion('cesar_jaramillo_distribuidos2','123456789')
```

__________________

Carolina Jiménez
German Gómez
