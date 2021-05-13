#!/bin/python3

import os 
import ipaddress
from getmac import get_mac_address

#a) Escreva código que, utilizando o módulo ipaddress, 
# imprima todos os endereços IP de uma rede com o prefixo 192.168.3.x
print ("Alinea a)")
conjuntoip=ipaddress.IPv4Network('192.168.3.0/24')
for ip in conjuntoip:
    print(f'{ip}')

#b) O módulo os do Python permite executar funções que estejam dependentes do sistema operativo. 
# Utilizando esse módulo e o módulo ipaddress, escreva código para executar um ping a toda a sua rede doméstica.
print ("Alinea b) e d)")
rede=input("Indique qual é o endereço de rede em formato CIDR (ex. 192.168.1.0/24): ")
ipdomestico=ipaddress.IPv4Network(rede)

for ips in ipdomestico:
    sinal = os.system("ping -c 1 " + str(ips) + " > /dev/null 2>&1")
    if sinal == 0:
        print("O endereço de IP " + (f'{ips}') + " está ligado.")
        print("O endereço MAC é " + get_mac_address(ip=sinal, network_request=True))
    else:
        print("O endereço de IP " + (f'{ips}') + " está desligado.")


#c) Adicione agora uma linha de código para que, no início da execução do programa, 
# seja mostrado o nome de utilizador atualmente com sessão iniciada. Esta funcionalidade é possível através do módulo
print("Nome de utilizador atualmente com sessão iniciada: ", os.getenv('LOGNAME'))

#d) O MAC Address de um dispositivo é o identificador único da placa de rede com que este se encontra ligado. 
# Utilize agora o módulo adicional get-mac (https://pypi.org/project/get-mac/), 
# desenvolvido pelo MIT, para obter e imprimir o MAC Address dos dispositivos que estejam online.

#realizado na alínea b

