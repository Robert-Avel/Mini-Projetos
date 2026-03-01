Lista = ["Nome1", "Nome2",]

def sistema(nome, list, adicionar_nome, novo):
    
    if nome in list:

        return "O Nome Já Está Na Lista"
    
    elif nome not in list:

        adicionar_nome
    
        if adicionar_nome == "Sim":
            
            novo_nome
            
            print(f"O Nome:{novo} Foi Adicionado Na Lista")

            return list.append(novo)
        
        
while True:
    
    nome = input("Digite Um Nome:")
    
    adicionar_nome = input("Gostaria De Adicionar Um Novo Nome?:")

    if adicionar_nome == "Nao":

        consulta = input("Gostaria De Fazer Uma Nova Consulta?:")

    else:

        consulta = 0

    if consulta == "Nao":

        print("Programa Finalizado")

        break

    elif consulta == "Sim":
            
        print("Nova Consulta")

    novo_nome = input("Novo Nome:")

    print(sistema(nome, Lista, adicionar_nome, novo_nome))

print(Lista)