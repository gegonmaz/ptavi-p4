#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys #este comando nos servirá para capturar los datos de la shell
import json
import time

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
                tiempo_activo = int(mensaje[3])
                #tiempo_actual = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))
                tiempo_actual = time.time()
                tiempo_expiracion = int(tiempo_actual) + tiempo_activo
                self.dicc_usuarios[mensaje[2]] = [IP, tiempo_expiracion]                
                if int(mensaje[3]) == 0 
                    del self.dicc_usuarios[mensaje[2]]
                    self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')                
            else:
                self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')
            # Añadimos caducidad a la conexion del cliente.
        tiempo_ahora = tiem.time()
        try:
            atributo = self.dicc_usuarios[IP]
            if tiempo_ahora >= time.strptime(atributo['expires']):
                del self.dicc_usuarios[IP] 
            print('Los usuarios actuales son: ', self.dicc_usuarios)
        self.register2json()
        self.json2registered()

    def register2json(self):
        """
        Este metodo creara un archivo con todos los usuarios registrados y sus
        direciones ips
        """
        fichero_reg = open('registered.json', 'w')
        json.dump(self.dicc_usuarios, fichero_reg, indent = 4)
        
    def json2registered(self):
        """
        Comprabara que el fichero no existe, y lo creara. 
        """
        try:
            with open('registered.json', 'r') as fichero_reg:
                self.dicc_usuarios = json.load(fichero_reg)
            
        except ValueError:
            json.dump(self.dicc_usuarios, fichero_reg) 
        
        
        
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
