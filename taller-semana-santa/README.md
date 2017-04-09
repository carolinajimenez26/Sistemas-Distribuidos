## Especificaciones

Implementar un sistema con la arquitectura que se encuentra en la imagen adjunta (cliente-servidor):

El requerimiento es el siguiente:

- Implementar un programa servidor que permita conectar varios clientes al tiempo(la conexión debe ser via sockets, se debe utilizar hilos para lograr la concurrencia de clientes, es decir varios a la vez).

- Cada que se conecte un cliente el servidor le debe enviar un mensaje con el numero de conexión, es decir: (hola, eres el cliente 1), (Hola, eres el cliente 2), (hola, eres el cliente 3)......(hola, eres el cliente), etc

![](https://github.com/carolinajimenez26/Sistemas-Distribuidos/blob/master/taller-semana-santa/Cliente_servidor_socket.png)
