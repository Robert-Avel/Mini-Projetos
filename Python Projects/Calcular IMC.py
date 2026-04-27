def calcular_imc(peso, altura): #Python 3.13.7

    imc = peso / (altura * altura)

    return imc

def classificar_imc(imc):

    if imc < 18.5:

        return "Abaixo Do Peso"
    
    elif imc >= 18.5 and imc < 25:

        return "Peso Normal"
    
    elif imc >= 25 and imc < 30:

        return "Sobrepeso"
    
    else:

        return "Obesidade"
    
while True:

    nome = input("(Nome Sair Para Sair)Nome:")

    if nome == "Sair":

        break

    peso = float(input("Peso:"))

    altura = float(input("Altura:"))

    imc = calcular_imc(peso, altura)

    classificar = classificar_imc(imc)

    print(f"Nome: {nome} \n Altura: {altura:.2f} \n Classificação: {classificar}")
