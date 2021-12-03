#client.py

#!/usr/bin/python                     

import socket                          
from time import sleep

s = socket.socket()                   
host = socket.gethostname()            
port = 12346                            
print("Conectando-se ao servidor")
s.connect((host, port))
print("Conectado.")

while True:
   print("Digite mensagem:")
   x = input()
   if x == 'SAIR':
        print('Desconectando.')
        s.send(x.encode())
        s.close()
        break
   s.send(x.encode())
   print("Mensagem enviada")
   print('Esperando resposta')
   data = s.recv(1024)
   if data.decode() == 'SAIR':
        print('Conexão encerrada.')
        s.close()
        break
   print('Resposta recebida:')
   print(data.decode())
