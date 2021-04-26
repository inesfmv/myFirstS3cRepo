#!/bin/python3
#coding: utf-8

import os 
import ipaddress


#a) Escreva código que, utilizando o módulo ipaddress, 
# imprima todos os endereços IP de uma rede com o prefixo 192.168.3.x
conjuntoip=ipaddress.IPv4Network('192.168.3.0/24')
for ip in conjuntoip:
    print(f'{ip}')

#b) O módulo os do Python permite executar funções que estejam dependentes do sistema operativo. 
# Utilizando esse módulo e o módulo ipaddress, escreva código para executar um ping a toda a sua rede doméstica.
localnetwork=ipaddress.ip_address
print (localnetwork)


#c) Adicione agora uma linha de código para que, no início da execução do programa, 
# seja mostrado o nome de utilizador atualmente com sessão iniciada. Esta funcionalidade é possível através do módulo os. 
user=os.getenv('LOGNAME')
print("Nome de utilizador atualmente com sessão iniciada: ", user)


#d) O MAC Address de um dispositivo é o identificador único da placa de rede com que este se encontra ligado. 
# Utilize agora o módulo adicional get-mac (https://pypi.org/project/get-mac/), 
# desenvolvido pelo MIT, para obter e imprimir o MAC Address dos dispositivos que estejam online.