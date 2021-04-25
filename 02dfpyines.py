#!/bin/bash
#coding: utf-8

import os 
import ipaddress

#a) Utilizando listas e um ciclo for, escreva código que guarde numa 
# lista o endereço IP dos primeiros 50 dispositivos numa rede. 
# No fim, imprima a lista de IPs.

conjuntoip=ipaddress.IPv4Network('192.168.1.0/29')
listacinq = [ ]
print ("alinea a")

for ip in conjuntoip:
    sinal = os.system("ping -c 1 " + str(ip) + " > /dev/null 2>&1")
    if sinal == 0:
        listacinq.append(f'{ip}')

listacinq=listacinq[:2]
print (listacinq)


# b) Escreva agora uma função para imprimir um IP por linha. 
# Para o efeito, utilize um ciclo for. A lista deverá receber a variável listaIPs como input.

print ("alinea b")

def imprip ():
    for ip in listacinq:
        print (f'{ip}')

imprip ()