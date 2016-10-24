#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar

# Este primer valor cogera la dir.IP

SERVER = str(sys.argv[1])

# este valor tratara de coger un PUERTO accesible

try:
    PORT = int(sys.argv[2])
except ValueError:
    print('Error en IP PUERTO')

# Aqui enviaremos texto (mensaje)--> join. nos divide el diccionario por ' '.

if str(sys.argv[3]) == 'register':
    nombre_usuario_sip = sys.argv[4]
    print('BIENVENIDO ' + nombre_usuario_sip)

# Ejercico 7--> vamos a añadirle tiempo de caducidad de la conexion

mensaje = 'REGISTER' + ' sip: '
LINE = mensaje + ' '.join(sys.argv[4:])

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando: " + LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')

    """
    Aqui le enviará al servidor el mensaje, y el servidor ya se encargara de
    ver si es un mensaje al chat, o si es una peticion de registro.
    """

    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))
    print("Socket terminado...")

# Cerramos todo--> siempre hay que cerrar todos los sockets

my_socket.close()
print("Proceso Finalizado.")
