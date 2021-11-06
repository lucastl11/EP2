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
    
 # EP2.5 - Posições possíveis da mão

def posicoes_possiveis(mesa, pecas):

 n = len(mesa)
 
 posicoes = []
 
 i = 0
 
 if n == 0:    
     while i < len(pecas):
       posicoes.append(i)
       i +=1
     return posicoes
 
 else:

  ponta_e = mesa[0][0]
  ponta_d = mesa[n-1][1]
 
  while i < len(pecas):
      if pecas[i][0] == ponta_e or pecas[i][0] == ponta_d:
         posicoes.append(i)
         i += 1
      elif pecas[i][1] == ponta_e or pecas[i][1] == ponta_d:
         posicoes.append(i)
         i += 1
      else:
         i += 1

  return posicoes 
 

print('Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.')

print('Vamos começar!!')


jogo_acabou = 1
while jogo_acabou != 0:

    jogadores_corretos = 0
    while jogadores_corretos == 0:

        jogadores = int(input('Quantos jogadores irão jogar? (2-4)'))

        if jogadores < 2 or jogadores > 4:
            print('Número de jogadores incorreto')
            jogadores_corretos == 0
        else:
            jogadores_corretos = 1

    pecas = cria_pecas()

    dic1= inicia_jogo( jogadores, pecas)

    monte = dic1['monte']
    print('Esse é o monte: ', monte)

    mesa = dic1['mesa']
    print('Essa é a mesa: ', mesa)

    player= dic1['jogadores'][0]
    print('Essa são as suas peças: ', player)

    todos_jog = []
    i = 0
    for jogador in dic1['jogadores']:
        todos_jog.append(i)
        i += 1

    #randomizar os jogadores    
    random.shuffle(todos_jog)

    print('A ordem do jogo será: ', todos_jog)
    ##player é o jogador 0 sempre

    while jogo_acabou != 0:
        #ainda tem muitas falhas nesse for
        for jogador in todos_jog:
            #para o player
            if jogador == 0:
                print('Sua vez: ')
                if not mesa:
                    print(player)
                    escolha_qlqr_peca = int(input('Escolha qualquer peça: '))
                    print('Mesa: ', adiciona_na_mesa(player[escolha_qlqr_peca],mesa))
                    del player[escolha_qlqr_peca]

                else:
                    posicoes = posicoes_possiveis(mesa, player)
                    print(posicoes)
                    escolha_peca = int(input('Escolha uma das peças possíveis: '))
                    print('Mesa: ', adiciona_na_mesa(player[escolha_peca],mesa))
                    del player[escolha_peca]

            #para os outros jogadores
            else:
                print('Vez do outro jogador')
                jogador_da_vez = dic1['jogadores'][jogador]
                print('pecas do jogador bot: ', jogador_da_vez)

                if not mesa:
                    peca_bot = random.choice(jogador_da_vez)
                    print('Mesa: ', adiciona_na_mesa(peca_bot,mesa))
                    del peca_bot
                else:
                    posicoes = posicoes_possiveis(mesa, jogador_da_vez)
                    peca_bot = random.choice(posicoes)
                    print(peca_bot)
                    print('Mesa: ',adiciona_na_mesa(jogador_da_vez[peca_bot],mesa))
                    del jogador_da_vez[peca_bot]
    
    
    
    
    
    
    
    ##print('Mesa: n/' , adiciona_na_mesa(pecas,'mesa'))
    
    round = 0
    jogo_acabou = 0