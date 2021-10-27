import random
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



print('Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.')

print('Vamos começar!!')

Jogadores = input('Quantos jogadores irão jogar? (2-4)')

