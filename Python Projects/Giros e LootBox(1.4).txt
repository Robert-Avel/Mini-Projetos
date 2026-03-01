import random

contagem = {"Bronze": 0, "Prata": 0, "Ouro": 0, "Platina": 0, "Diamante": 0, "Esmeralda": 0}

giros = 0

quantidade_de_giros = 0

Codigo = 0

def loot(Box):

    if Box >= 50:

        print("Você Ganhou Bronze")

        contagem["Bronze"] += 1

    elif Box >= 30 and Box < 50:

        print("Você Ganhou Prata")

        contagem["Prata"] += 1

    elif Box < 30 and Box >= 15:

        print("Você Ganhou Ouro")

        contagem["Ouro"] += 1

    elif Box < 15 and Box >= 5:

        print("Você Ganhou Platina")

        contagem["Platina"] += 1

    elif Box < 5 and Box >= 2:

        print("Você Ganhou Diamante, Parabéns")

        contagem["Diamante"] += 1

    else:

        print("Você Ganhou ESMERALDA, PARABÉNS")

        contagem["Esmeralda"] += 1

while True:

    Girar = input("Digite Qualquer Coisa Para Ver Os Comandos:")

    if Girar == "N":

        break

    elif Girar == "S" and quantidade_de_giros > 0:

        Box = random.randint(1, 100)

        loot(Box)

        giros += 1

        quantidade_de_giros -= 1

    elif Girar == "M" and quantidade_de_giros > 99:

        print("Girando 100")
        
        for i in range(1, 101):
         
         Box = random.randint(1, 100)

         loot(Box)

        giros += 100

        quantidade_de_giros -= 100

    elif Girar == "M" and quantidade_de_giros < 100 or Girar == "S" and quantidade_de_giros < 1:

            print("Você Não Possui Giros O Suficiente")

    elif Girar == "Giros":

        print(f"Você Ja Girou:{giros} Vezes")

    elif Girar == "Quantos":

        print(f" Bronze:{contagem['Bronze']} \n Prata:{contagem['Prata']} \n Ouro:{contagem['Ouro']} \n Platina:{contagem['Platina']} \n Diamante:{contagem['Diamante']} \n Esmeralda:{contagem['Esmeralda']}")

    elif Girar == "Limpar":

        giros = 0
        
        contagem["Bronze"] = 0
        contagem["Prata"] = 0
        contagem["Ouro"] = 0
        contagem["Platina"] = 0
        contagem["Diamante"] = 0
        contagem["Esmeralda"] = 0


        print("A Quantidade De Giros E a Quantidade De Loots Foram Reiniciados")

    elif Girar == "Code":

        Codigo = input("Digite Um Código:")

        if Codigo == "1KSPINS":

           quantidade_de_giros += 1000

           print(f"Parabéns, Você Resgatou 1000 Giros")

        else:

            print(f"O Código ({Codigo}) É Inexistente")

    elif Girar == "Quantos Giros":

        print(f"Você Tem:{quantidade_de_giros} Giros")

    else:

        print(f"Você Só Pode Usar Os Comandos: \n (S) Para Roletar 1 Vez \n (N) Para Encerrar O Script \n (M) Para Roletar 100 Vezes \n (Giros) Para Ver Quantas Vezes Você Roletou \n (Quantos) Para Quantos Premios Você Recebeu De Cada Tipo \n (Limpar) Para Limpar Seus Giros e Premios \n (Code) Para Digitar Algum Código \n (Quantos Giros) Para Saber Quantas Vezes Você Pode Roletar")