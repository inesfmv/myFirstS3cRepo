#!/bin/python3
#coding: utf-8

import os
import glob

# a) Usando o módulo glob do Python, escreva código para listar todos os ficheiros de um diretório.
direct = os.getcwd()
print("A diretoria atual é: ", direct)

file=glob.glob('*.*')
print("Dentro de ", direct, "tens os seguintes ficheiros: ", file)

# b) Altere o código para listar apenas ficheiros com a extensão .py (Python)
file=glob.glob('*.py')
print("Dentro de ", direct, "tens os seguintes ficheiros em python: ", file)

# c) Altere o código para gravar o output num ficheiro de texto, para além de a imprimir no terminal.
ficheiro = open("listadepy.txt", 'w')
ficheiro.write(str(file))
ficheiro.close()
