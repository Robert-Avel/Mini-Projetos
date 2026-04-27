from random import randint

mapa:list = [["~"] * 5 for i in range(5)]
tesouro:list = [randint(0,4),randint(0,4)]
fim_de_jogo:bool = False

def validar_coordenadas(coord_lin,coord_col):
    if coord_lin in range(5) or coord_col in range(5):
        if coord_col == 0 or coord_lin == 0:
            
            if coord_col == 0: coord_col += 1
            elif coord_lin == 0: coord_lin += 1
        else:
            if coord_col != 0: coord_col -= 1
            if coord_lin != 0: coord_lin -= 1
            
        return coord_lin,coord_col
    else: return False,False
        
def validar_jogo(fim_de_jogo,coord_lin,coord_col,tesouro):
    
    if coord_lin not in range(5) or coord_col not in range(5):
        print("Coordenadas inválidas. Tente novamente.")
        return False
    
    if coord_lin == tesouro[0] and coord_col == tesouro[1]:
        mapa[coord_lin][coord_col] = "T"
        print("Parabéns, você encontrou o tesouro!")
        [print(' '.join(map(str,linha))) for linha in mapa]
        fim_de_jogo = True
        return fim_de_jogo
        
def atualizar_mapa(mapa,coord_lin,coord_col,tesouro):
    if mapa[coord_lin] != tesouro[0]:
        mapa[coord_lin][coord_col] = "X"
        
        if coord_lin < tesouro[0]:
            mapa[coord_lin][coord_col] = "S"
        elif coord_lin > tesouro[0]:
            mapa[coord_lin][coord_col] = "N"
        if coord_col < tesouro[1]:
            mapa[coord_lin][coord_col] = "L"
        elif coord_col > tesouro[1]:
            mapa[coord_lin][coord_col] = "O"
        for i in range(5):
            print(i+1,' '.join(map(str,mapa[i])))
        [print(i, end=' ') for i in range(6)]
    
while not fim_de_jogo:
    try:
        coord_lin:int = int(input("\nDigite as coordenadas do tesouro (linha e coluna)\n"
                            "Linha:"))
        coord_col:int = int(input("Coluna:"))
    except ValueError:
        print("Coordenadas inválidas. Tente novamente.")
        continue
    
    coord_lin, coord_col = validar_coordenadas(coord_lin,coord_col)
    if isinstance(coord_lin, bool):
        print("Coordenadas inválidas. Tente novamente.")
        continue
    
    fim_de_jogo = validar_jogo(fim_de_jogo,coord_lin,coord_col,tesouro)
    
    if not fim_de_jogo:
        atualizar_mapa(mapa,coord_lin,coord_col,tesouro)
