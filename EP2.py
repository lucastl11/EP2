import random

# EP2.1 - Criando peças de dominó

def cria_pecas():
    pecas = []
    i = 0
    j = 0
    c = 1
    m = 0
    while m < 28:
        if i > 6:
            i = 0
            i += c
            c += 1
            j += 1        
        pecas.append([j,i])
        m += 1
        i += 1

    random.shuffle(pecas)
    return pecas

# EP2.2 - Iniciando o Jogo de Dominó

def inicia_jogo(jogadores, pecas):

    # dicionário:
    dic = {
    'jogadores':{},
    'monte': [],
    'mesa':[]    
    }

    # lista jogadores, mesa e monte:
    j0 = []
    j1 = []
    j2 = []
    j3 = []
    mesa = []
    monte = []

    # divisão das cartas (2-4 jogadores):

    i = 0
    if jogadores == 2:
        while i < 7:
            j0.append(pecas[i])
            i += 1
        while i < 14:
            j1.append(pecas[i])
            i += 1
        while i < 28:
            monte.append(pecas[i])
            i += 1    
       
        dic['jogadores'][0] = j0    
        dic['jogadores'][1] = j1
        dic['monte'] = monte
        dic['mesa'] = mesa 

    i = 0
    if jogadores == 3:
        while i < 7:
            j0.append(pecas[i])
            i += 1
        while i < 14:
            j1.append(pecas[i])
            i += 1
        while i < 21:
            j2.append(pecas[i])
            i += 1  
        while i < 28:
            monte.append(pecas[i])
            i += 1          
        
        dic['jogadores'][0] = j0    
        dic['jogadores'][1] = j1
        dic['jogadores'][2] = j2
        dic['monte'] = monte 
        dic['mesa'] = mesa 
    
    i = 0
    if jogadores == 4:
        while i < 7:
            j0.append(pecas[i])
            i += 1
        while i < 14:
            j1.append(pecas[i])
            i += 1
        while i < 21:
            j2.append(pecas[i])
            i += 1  
        while i < 28:
            j3.append(pecas[i])
            i += 1          
        
        dic['jogadores'][0] = j0    
        dic['jogadores'][1] = j1
        dic['jogadores'][2] = j2
        dic['jogadores'][3] = j3
        dic['monte'] = monte
        dic['mesa'] = mesa      

    return dic 

# EP2.4 - Soma peças do dominó

def soma_pecas(pecas):
    soma = 0
    if pecas:       
        for p in pecas:
            soma += p[0] + p[1]
        return soma
    else:
        return 0
        
def adiciona_na_mesa(peca,mesa):
    if not mesa:
        mesa.append(peca)
        return mesa
        
    ##Ultima peca e primeira peca   
    up = mesa[-1][1]
    pp = mesa[0][0]    
    
    ##Para a esquerda ou direita
    for p in peca:
        if p == pp or p == up:
            if p in mesa[0]:
                posicao_m = mesa[0].index(p)
                if posicao_m == 0:
                    if p == peca[1]:
                        mesa.insert(0,peca)
                    if p == peca[0]:
                        peca[0],peca[1] = peca[1], peca[0]
                        mesa.insert(0,peca)
            if p in mesa[-1]:
                posicao_m = mesa[-1].index(p)
                if posicao_m == 1: 
                    if p == peca[0]:
                        mesa.append(peca)
                    if p == peca[1]:
                        peca[0],peca[1] = peca[1], peca[0]
                        mesa.append(peca)
        
    return mesa    

# EP2.3 - Quem ganhou no dominó?

def verifica_ganhador(dicionario):
    
 ganhou = True 
 for jogador in dicionario.keys():
        
        pecas = dicionario[jogador]

        if pecas == []:
            return jogador
        else:
            ganhou = False 
            
 if ganhou == False:
     return -1



    
print('Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.')

print('Vamos começar!!')

Jogadores = input('Quantos jogadores irão jogar? (2-4)')

