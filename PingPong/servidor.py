#server.py
#!/usr/bin/python                           

import socket                               
from time import sleep

s = socket.socket()                       
host = socket.gethostname()             
port = 12346                             
s.bind((host, port))
print('Esperando conexao')
s.listen()             
c, addr = s.accept()
print('Conectado')
while True:
   print('Esperando mensagem')
   data = c.recv(1024)
   if data.decode() == 'SAIR':
        print('Conexão encerrada.')
        print('Esperando conexao')
        s.listen()             
        c, addr = s.accept()
        print('Conectado')
   else:     
       print('Mensagem recebida:')
       print(data.decode())
       print('Digite resposta:')
       x = input()
       if x == 'SAIR':
            print('Desconectando.')
            c.sendall(x.encode())
            s.close() 
            break
       c.sendall(x.encode())