#!/bin/bash
#coding: utf-8

import os 
import ipaddress

listaip=ipaddress.IPv4Network('192.168.1.0/24')

for ip in listaip:
    print(f'{ip}')

#a) Utilizando listas e um ciclo for, escreva código que guarde numa lista o endereço IP 
# dos primeiros 50 dispositivos numa rede. No fim, imprima a lista de IPs.


# b) Escreva agora uma função para imprimir um IP por linha. 
# Para o efeito, utilize um ciclo for. A lista deverá receber a variável listaIPs como input.