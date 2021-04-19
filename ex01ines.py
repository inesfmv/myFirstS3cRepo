clientes = int(input("Quantos clientes estão dentro da loja: "))
if clientes <= 5:
    print ("Risco de contágio: Baixo")
elif clientes > 5 and clientes <= 10:
    print ("Risco de contágio: Médio")
elif clientes > 10 and clientes <= 15:
    print ("Risco de contágio: Elevado")
else:
    print ("Risco de contágio: Extremo")