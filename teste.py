import random

# Definição das funções:

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

# EP2.4 - Soma peças do dominó

def soma_pecas(pecas):
    soma = 0
    if pecas:       
        for p in pecas:
            soma += p[0] + p[1]
        return soma
    else:
        return 0

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

# EP2.6 - Adicionando peças a mesa num jogo de dominó
        
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

# Início do jogo

print('.:::Dominó:::.')

print ('Design de Software 2021.2 - Insper')

print('Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.')

print('Vamos começar!')

jogadores = int(input('Quantidade de jogadores (2-4):'))

pecas = cria_pecas() # Passo 1: criar as peças do jogo.

dicionario = inicia_jogo(jogadores, pecas) # Passo 2: distribuir as peças entre os jogadores e o monte.

mesa = dicionario['mesa']
monte = dicionario['monte']

lista_jogadores = []
i = 0
for jogador in dicionario['jogadores']:
        lista_jogadores.append(i)
        i += 1

# Início das jogadas

continua = -1


while continua == -1: # Situação 1: o jogo continua.
    for jogador in lista_jogadores:
            # Vez do jogador humano:
            if jogador == 0:
                print('Mesa:', mesa)
                print('Jogador da vez: você está com {} peças'.format(len(dicionario['jogadores'][0])))
                print(dicionario['jogadores'][0])

                posicoes = posicoes_possiveis(mesa, dicionario['jogadores'][0]) # Verificar se há posições possíveis.
                
                if posicoes != []: # Há posições possíveis
                   print('Posições possíveis:', posicoes)
                   jogada = int(input('Escolha a peça:'))

                   while jogada not in posicoes:
                       print('Posição inválida') # VERIFICAR CÓDIGO
                       print('Escolha entre as posições possíveis!')
                       jogada = int(input('Escolha a peça: '))
                   if jogada in posicoes:
                       adiciona_na_mesa(dicionario['jogadores'][0][jogada],mesa)
                       print ('Colocou:', dicionario['jogadores'][0][jogada])
                       del dicionario['jogadores'][0][jogada]
                while posicoes == []: # Não há posições possíveis
                    print('Não tem peças possíveis') 
                    print('Retirar do monte')
                    aleatoria = random.choice(monte)
                    del monte[aleatoria]
                    dicionario['jogadores'][0].append(aleatoria)
                # Verificar se jogador humano ganhou  
                continua = verifica_ganhador(dicionario)
            # Vez do(s) jogador(es) automatizado(s):
            else:
                print('Mesa:', mesa)
                print('Jogador da vez: jogador {} com {} peças'.format(jogador, len(dicionario['jogadores'][jogador])))

                posicoes = posicoes_possiveis(mesa, dicionario['jogadores'][jogador]) # Verificar se há posições possíveis.
                
                if posicoes != []: # Há posições possíveis
                      aleatoria1 = random.choice(posicoes)
                      adiciona_na_mesa(dicionario['jogadores'][jogador][aleatoria1],mesa)
                      print ('Colocou:', dicionario['jogadores'][jogador][aleatoria1])
                      del dicionario['jogadores'][jogador][aleatoria1]
                while posicoes == []: # Não há posições possíveis
                    print('Não tem peças possíveis') 
                    print('Vai retirar do monte')
                    aleatoria = random.choice(monte)
                    x = monte.index(aleatoria)
                    del monte[x]
                    dicionario['jogadores'][jogador].append(aleatoria)
                # Verificar se jogador automatizado ganhou  
                continua = verifica_ganhador(dicionario)
if continua == -1 and monte == []: # Situação 2: o jogo travou e vai para a soma das peças.

 print('O jogo fechou sem nenhum jogador zerar as peças!')
 print('Contabilizando peças...')
 print('Vencedor(es): ', )

if continua != -1: # # Situação 3: algum jogador ganhou.
   print('O vencedor é :', continua)