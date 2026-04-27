def multiplicar(numero, multiplo):

    if numero <= 10 and numero >= 1:

        for multiplo in range(1, 11):

            print(f"Numero:{numero} X {multiplo} = {numero * multiplo}")

    elif numero < 1:

        print("O Número Deve Ser Maior Que 1")
    
    elif numero > 10:

        print("O Número Deve Ser Menor Que 10")
    
while True:

    numero = int(input("Numero:"))

    if numero == 0:

        break
  
    multiplo = 0

    tabuada = multiplicar(numero, multiplo)