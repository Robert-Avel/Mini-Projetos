import random

numero = random.randint(1, 20)

tentativas = 5

def sort(numero, numero1, tentativas):

    if numero1 > numero:

        print(f"O Numero é Menor Que {numero1} ")

        tentativas -= 1

        print(f"Você Tem {tentativas} Tentativas")

    elif numero1 < numero:

        print(f"O Numero é Maior Que {numero1}")

        tentativas -= 1

        print(f"Você Tem {tentativas} Tentativas")

    else:

        print(f"O Numero {numero1} Esta Correto✅")

    return tentativas


while True:

    numero1 = int(input("Acerte O Numero:"))

    tentativas = sort(numero, numero1, tentativas)

    if tentativas <= 0:

        print(f"Você Perdeu o Numero Era:{numero}")

        break

    elif numero1 == numero:

        break

