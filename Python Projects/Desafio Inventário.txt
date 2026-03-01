inventario = []

def armazenamento(armazenar_item,armazem, inventario):

    if armazenar_item in inventario:

        print("Este Item Já Esta No Inventário")

    elif armazenar_item not in inventario and armazenar_item != "Remover" and armazem < 37:

        inventario.append(armazenar_item)

        print(f" Item Armazenado \n Você Só Pode Armazenar Mais:{35 -armazen} Itens\n Seus Itens No Inventário São{inventario}")

    elif armazem >= 36:

        print("Inventário Cheio")

while True:

    guardar_item = input("Você Gostaria De Guardar Qual Item?:")

    armazen = len(inventario)

    if guardar_item == "Nada":

        print(f"Você Guardou Os Itens:\n{inventario}")

        break

    elif guardar_item == "Remover":

        remover_iten = input("Qual Item Deve Ser Removido?:")

        inventario.remove(remover_iten)

        armazen -= 1

        print(f" Item Removido \n Você Só Pode Armazenar Mais:{35- armazen} Itens\n Seus Itens No Inventário São{inventario}")

    armazenamento(guardar_item, armazen, inventario)
