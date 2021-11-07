import random
import time

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
        
def adiciona_na_mesa(peca, mesa):
    if mesa == []:
        mesa = [peca]
        return mesa
    ponta_esquerda = mesa[0][0]
    ponta_direita = mesa[-1][1]
    if peca[1] == ponta_esquerda:
        mesa = [peca] + mesa
    elif peca[0] == ponta_esquerda:
        peca = [peca[1], peca[0]]
        mesa = [peca] + mesa
    elif peca[0] == ponta_direita:
        mesa = mesa + [peca]
    else:
        peca = [peca[1], peca[0]]
        mesa = mesa + [peca]
    return mesa
        

# Início do jogo

print('.:::Dominó:::.')
time.sleep(0.75)

print ('Design de Software 2021.2 - Insper')
time.sleep(0.75)

print('Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.')
time.sleep(0.75)

print('Vamos começar!')
time.sleep(0.75)

jogadores_corretos = 0
while jogadores_corretos == 0:

    jogadores = int(input('Quantos jogadores irão jogar? (2-4)'))

    if jogadores < 2 or jogadores > 4:
        print('Número de jogadores incorreto')
        jogadores_corretos == 0
    else:
        jogadores_corretos = 1

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
                time.sleep(1)
                print('Você está com {} peças'.format(len(dicionario['jogadores'][0])))
                time.sleep(1)
                print(dicionario['jogadores'][0])
                time.sleep(1)

                posicoes = posicoes_possiveis(mesa, dicionario['jogadores'][0]) # Verificar se há posições possíveis.
                time.sleep(1)
                
                if posicoes: # Há posições possíveis
                   print('Posições possíveis:', posicoes)
                   jogada = int(input('Escolha a peça: '))
                   time.sleep(0.5)
                   while jogada not in posicoes:
                       print('Posição inválida') # VERIFICAR CÓDIGO
                       print('Escolha entre as posições possíveis!')
                       jogada = int(input('Escolha a peça: '))
                   if jogada in posicoes:
                       mesa = adiciona_na_mesa(dicionario['jogadores'][0][jogada],mesa)
                       print ('Colocou: ', dicionario['jogadores'][0][jogada])
                       time.sleep(0.5)
                       del dicionario['jogadores'][0][jogada]

                while not posicoes: # Não há posições possíveis
                    print('Não tem peças possíveis') 
                    print('Retirar do monte')

                    if monte:
                        aleatoria = random.choice(monte)
                        peca_aleatoria = monte.index(aleatoria)
                        dicionario['jogadores'][0].append(aleatoria)
                        print(dicionario['jogadores'][0])
                        del monte[peca_aleatoria]
                        posicoes = posicoes_possiveis(mesa, dicionario['jogadores'][0])
                        time.sleep(0.5)
                        print(posicoes)
                        if posicoes:
                            peca_dicionario = dicionario['jogadores'][0].index(aleatoria)
                            mesa = adiciona_na_mesa(dicionario['jogadores'][0][peca_dicionario],mesa)
                            print ('Colocou: ', dicionario['jogadores'][0][peca_dicionario])
                            time.sleep(0.5)
                    else:
                        print('Acabaram as peças do monte')
                # Verificar se jogador humano ganhou  
                continua = verifica_ganhador(dicionario)
            # Vez do(s) jogador(es) automatizado(s):
            else:
                print('Mesa:', mesa)
                time.sleep(1)
                print('Jogador {} com {} peças'.format(jogador, len(dicionario['jogadores'][jogador])))
                time.sleep(1)

                posicoes = posicoes_possiveis(mesa, dicionario['jogadores'][jogador]) # Verificar se há posições possíveis.
                time.sleep(1)
                
                if posicoes: # Há posições possíveis
                      aleatoria1 = random.choice(posicoes)
                      mesa = adiciona_na_mesa(dicionario['jogadores'][jogador][aleatoria1],mesa)
                      print ('Colocou:', dicionario['jogadores'][jogador][aleatoria1])
                      time.sleep(0.5)
                      del dicionario['jogadores'][jogador][aleatoria1]
                while not posicoes and monte != []: # Não há posições possíveis
                    print('Não tem peças possíveis')
                    time.sleep(0.5) 
                    print('Vai retirar do monte')
                    time.sleep(0.5)
                    if monte:
                        aleatoria = random.choice(monte)
                        peca_aleatoria = monte.index(aleatoria)
                        del monte[peca_aleatoria]
                        dicionario['jogadores'][jogador].append(aleatoria)
                        posicoes = posicoes_possiveis(mesa, dicionario['jogadores'][jogador])
                        print(posicoes)
                        time.sleep(0.5)
                        if posicoes:
                            peca_dicionario = dicionario['jogadores'][jogador].index(aleatoria)
                            mesa = adiciona_na_mesa(dicionario['jogadores'][jogador][peca_dicionario],mesa)
                            print ('Colocou: ', dicionario['jogadores'][jogador][peca_dicionario])
                            time.sleep(0.5)
                    else:
                        print('Acabaram as peças do monte')
                # Verificar se jogador automatizado ganhou  
            continua = verifica_ganhador(dicionario['jogadores'])

            if continua != -1: # # Situação 3: algum jogador ganhou.
                print('O jogo acabou!')
                print('O vencedor é o jogador: ', continua)
                break

if continua == -1 and monte == []: # Situação 2: o jogo travou e vai para a soma das peças.

    print('O jogo fechou sem nenhum jogador zerar as peças!')
    print('Contabilizando peças...')
    lista_soma = []
    for jogador in dicionario['jogadores']:
        pecas_jogadores = []
        for peca in dicionario['jogadores'][jogador]:
            pecas_jogadores.append(peca)
        soma = soma_pecas(pecas_jogadores)
        lista_soma.append(soma)
        print('A soma das peças do jogador {} é: '.format(jogador), soma)

    for soma in lista_soma:
        jogador = lista_soma.count(soma)
        if jogador > 1:
            print('O jogo empatou!')
            break
            
    vencedor = max(lista_soma)
    jogador_vencedor = lista_soma.index(vencedor)    
    print('Vencedor(es): ', jogador_vencedor )
