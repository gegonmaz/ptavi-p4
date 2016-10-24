#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys #este comando nos servirá para capturar los datos de la shell

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    
    dicc_usuarios = {} #Variable de uso general por tanto fuera de clase.
    def handle(self):
        #dicc_usuarios = {} #Variable de uso general por tanto fuera de clase.
        self.wfile.write(b"Hemos recibido tu peticion")
        #El servidor tambien tiene que enviar un mensaje de respuesta a REGIS.
        IP = str(self.client_address[0])
        print('Dir. IP del cliente: ' + IP)
        PUERTO = str(self.client_address[1])
        print('Puerto donde escucha cliente: ' + PUERTO) 
        #print(self.client_address)                
        for line in self.rfile:
            mensaje = line.decode('utf-8').split()
            #Dividimos el mensaje para buscar las palabras clave REGISTER/SIP
            print("El cliente nos manda ", line.decode('utf-8'))
            #Aqui es donde el servidor lee linea a linea lo que recibe de cli.
            if mensaje[0] == 'REGISTER':
                self.dicc_usuarios[mensaje[2]] = IP              
                if int(mensaje[3]) == 0:
                    del self.dicc_usuarios[mensaje[2]]
                    self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')
                else:
                    self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')
            # Añadimos caducidad a la conexion del cliente. 
            print('Los usuarios actuales son: ', self.dicc_usuarios)

if __name__ == "__main__":
    """
    Tendremos que cambiar la linea siguiente para que coja el 
    puerto y la dir.IP
    """
    #serv = socketserver.UDPServer(('', 6001), EchoHandler)
    try:
        serv = socketserver.UDPServer(('',int(sys.argv[1])), SIPRegisterHandler)
        print('Lanzando servidor UDP de eco...')        
        serv.serve_forever()    
    except ValueError:
        print('PUERTO NO ENCONTRADO')
    except KeyboardInterrupt:       # Ctrl + C--> interrumpimos servidor
        print("Finalizado servidor")
