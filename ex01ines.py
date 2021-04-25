

clientes = int(input("Quantos clientes estao dentro da loja: "))
if clientes <= 5:
    print ("Risco de contagio: Baixo")
elif clientes > 5 and clientes <= 10:
    print ("Risco de contagio: Medio")
elif clientes > 10 and clientes <= 15:
    print ("Risco de contagio: Elevado")
else:
    print ("Risco de contagio: Extremo")