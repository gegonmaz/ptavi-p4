#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys #este comando nos servirá para capturar los datos de la shell

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        self.wfile.write(b"Hemos recibido tu peticion")
        #IP = str(self.client_address[0])
        #print('Dir. IP del cliente: ' + IP)
        #PUERTO = int(self.client_address[1])
        #print('Puerto donde escucha cliente: ' + PUERTO) 
        print(self.client_address)
        for line in self.rfile:
            print("El cliente nos manda ", line.decode('utf-8'))

if __name__ == "__main__":
    """
    Tendremos que cambiar la linea siguiente para que coja el puerto y la dir.IP
    """
    #serv = socketserver.UDPServer(('', 6001), EchoHandler)
    try:
        serv = socketserver.UDPServer(('',int(sys.argv[1])), EchoHandler)
        print('Lanzando servido UDP de eco...')        
        serv.serve_forever()    
    except ValueError:
        print('PUERTO NO ENCONTRADO')
    except KeyboardInterrupt:       # Ctrl + C--> interrumpimos servidor
        print("Finalizado servidor")
