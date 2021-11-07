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

jogadores = int(input('Quantidade de jogadores (2-4):'))
time.sleep(0.75)

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

random.shuffle(lista_jogadores)
print('A ordem do jogo será: ', lista_jogadores)
time.sleep(0.75)
print('Você é o jogaddor 0')
time.sleep(0.75)

continua = -1
lista_posicoes_jogadores = [0] * len(lista_jogadores)
while continua == -1: # Situação 1: o jogo continua.
    for jogador in lista_jogadores:

        # Vez do jogador humano:
        if jogador == 0:
            print('\n')
            print('Mesa:', mesa)
            print('\n')
            time.sleep(1)
            print('Jogador da vez: você está com {} peças'.format(len(dicionario['jogadores'][0])))
            time.sleep(0.75)
            print(dicionario['jogadores'][0])
            time.sleep(0.75)

            posicoes = posicoes_possiveis(mesa, dicionario['jogadores'][0]) # Verificar se há posições possíveis.
            
            if posicoes != []: # Há posições possíveis
                print('Posições possíveis:', posicoes)
                time.sleep(0.75)
                jogada = int(input('Escolha a peça: '))
                time.sleep(0.75)

                while jogada not in posicoes:
                    print('Posição inválida') 
                    print('Escolha entre as posições possíveis!')
                    time.sleep(1)
                    jogada = int(input('Escolha a peça:'))
                    time.sleep(0.75)
                if jogada in posicoes:
                    mesa = adiciona_na_mesa(dicionario['jogadores'][0][jogada],mesa)
                    print ('Colocou: ', dicionario['jogadores'][0][jogada])
                    time.sleep(0.75)
                    del dicionario['jogadores'][0][jogada]
            else:
                while posicoes_possiveis(mesa, dicionario['jogadores'][0]) == [] and monte != []: # Não há posições possíveis
                    print('\n')
                    print('Não tem peças possíveis') 
                    print('Retirar do monte')
                    time.sleep(0.75)
                    pergunta = input("Pressione Enter para continuar...")
                    dicionario['jogadores'][0].append(monte[0])
                    # retira a primeira peça do monte
                    monte.pop(0)
                    posicoes = posicoes_possiveis(mesa, dicionario['jogadores'][0])
                    
                    
                if posicoes_possiveis(mesa, dicionario['jogadores'][0]) != []:
                    mesa = adiciona_na_mesa(dicionario['jogadores'][0][-1],mesa)
                    print ('Colocou: ', dicionario['jogadores'][0][-1])
                    time.sleep(0.75)
                    dicionario['jogadores'][0].pop(-1)
                    
                
                elif monte == []:
                    print('\n')
                    print("Não há peças no monte")
                    print("Jogador passou a vez")
                    time.sleep(1.5)

            lista_posicoes_jogadores[0] = posicoes
            # Verificar se jogador humano ganhou  
            

        # Vez do(s) jogador(es) automatizado(s):
        else:
            print('\n')
            print('Mesa:', mesa)
            print('\n')
            time.sleep(1)
            print('Jogador da vez: jogador {} está com {} peças'.format(jogador, len(dicionario['jogadores'][jogador])))
            time.sleep(0.75)

            posicoes = posicoes_possiveis(mesa, dicionario['jogadores'][jogador]) # Verificar se há posições possíveis.
            
            if posicoes != []: # Há posições possíveis
                aleatoria1 = random.choice(posicoes)
                mesa = adiciona_na_mesa(dicionario['jogadores'][jogador][aleatoria1],mesa)
                print ('Colocou: ', dicionario['jogadores'][jogador][aleatoria1])
                time.sleep(0.75)
                del dicionario['jogadores'][jogador][aleatoria1]
            
            else:
                while posicoes_possiveis(mesa, dicionario['jogadores'][jogador]) == [] and monte != []: # Não há posições possíveis
                    print('\n')
                    print('Não tem peças possíveis')
                    time.sleep(0.25) 
                    print('Retirar do monte')
                    time.sleep(1)
                    dicionario['jogadores'][jogador].append(monte[0])
                    # retira a primeira peça do monte
                    monte.pop(0)
                    posicoes = posicoes_possiveis(mesa, dicionario['jogadores'][jogador])
                   
                if posicoes_possiveis(mesa, dicionario['jogadores'][jogador]) != []:
                    mesa = adiciona_na_mesa(dicionario['jogadores'][jogador][-1],mesa)
                    print ('Colocou: ', dicionario['jogadores'][jogador][-1])
                    time.sleep(0.75)
                    dicionario['jogadores'][jogador].pop(-1)
                    

                elif monte == []:
                    print('\n')
                    print("Jogador não possui peças")
                    time.sleep(0.25)
                    print('Passou a vez')
                    time.sleep(1)

            lista_posicoes_jogadores[jogador] = posicoes

            # Verificar se jogador humano ganhou  

        continua = verifica_ganhador(dicionario['jogadores'])

        verifica_lista_posicoes = all(elem == [] for elem in lista_posicoes_jogadores)
        resultado = False
        if verifica_lista_posicoes:
            resultado = True

        if continua != -1:  # Situação 3: algum jogador ganhou.
            print('O vencedor é o jogador: ', continua)
            break

        elif continua == -1 and monte == [] and resultado == True: # Situação 2: o jogo travou e vai para a soma das peças. 
            print('\n')       
            print('O jogo fechou sem nenhum jogador zerar as peças!')
            time.sleep(0.75)
            print('Contabilizando peças...')
            time.sleep(2)
            
            # Aqui entra na parte "empates"
            
            if jogadores == 2:

                soma0 = soma_pecas(dicionario['jogadores'][0])
                soma1 = soma_pecas(dicionario['jogadores'][1])

                # 1 jogador vence:
                if soma0 < soma1:
                    print('Vencedor(es) é(são): 0')
                if soma1 < soma0:
                    print('Vencedor(es) é(são): 1')
                # 2 jogadores vencem:     
                if soma0 == soma1:
                    print('Vencedor(es) é(são): 0, 1')

                continua = -2
                break

            if jogadores == 3:

                soma0 = soma_pecas(dicionario['jogadores'][0])
                soma1 = soma_pecas(dicionario['jogadores'][1])
                soma2 = soma_pecas(dicionario['jogadores'][2])

                # 1 jogador vence:
                if soma0 < soma1 and soma0 < soma2:
                    print('Vencedor(es) é(são): 0')
                if soma1 < soma0 and soma1 < soma2:
                    print('Vencedor(es) é(são): 1')
                if soma2 < soma0 and soma2 < soma1:
                    print('Vencedor(es) é(são): 2') 
                if soma2 < soma0 and soma2 < soma1:
                    print('Vencedor(es) é(são): 2') 

                # 2 jogadores vencem:          
                if soma0 == soma1 and soma0 < soma2:
                    print('Vencedor(es) é(são): 0, 1')    
                if soma0 == soma2 and soma0 < soma1:
                    print('Vencedor(es) é(são): 0, 2')    
                if soma1 == soma2 and soma1 < soma0:
                    print('Vencedor(es) é(são): 1, 2')  

                # 3 jogadores vencem:          
                if soma0 == soma1 and soma0 == soma2:
                    print('Vencedor(es) é(são): 0, 1, 2') 

                continua = -2
                break   

            if jogadores == 4:

                soma0 = soma_pecas(dicionario['jogadores'][0])
                soma1 = soma_pecas(dicionario['jogadores'][1])
                soma2 = soma_pecas(dicionario['jogadores'][2])
                soma3 = soma_pecas(dicionario['jogadores'][3])

                # 1 jogador vence:
                if soma0 < soma1 and soma0 < soma2 and soma0 < soma3:
                    print('Vencedor(es) é(são): 0')
                if soma1 < soma0 and soma1 < soma2 and soma1 < soma3:
                    print('Vencedor(es) é(são): 1')
                if soma2 < soma0 and soma2 < soma1 and soma2 < soma3:
                    print('Vencedor(es) é(são): 2') 
                if soma3 < soma0 and soma3 < soma1 and soma3 < soma2:
                    print('Vencedor(es) é(são): 3') 

                # 2 jogadores vencem:
                if soma0 == soma1 and soma0 < soma2 and soma0 < soma3:
                    print('Vencedor(es) é(são): 0, 1')    
                if soma0 == soma2 and soma0 < soma1 and soma0 < soma3:
                    print('Vencedor(es) é(são): 0, 2') 
                if soma0 == soma3 and soma0 < soma1 and soma0 < soma2:
                    print('Vencedor(es) é(são): 0, 3')        
                if soma1 == soma2 and soma1 < soma0 and soma1 < soma3:
                    print('Vencedor(es) é(são): 1, 2')    
                if soma1 == soma3 and soma1 < soma0 and soma1 < soma2:
                    print('Vencedor(es) é(são): 1, 3') 
                if soma2 == soma3 and soma2 < soma0 and soma2 < soma1:
                    print('Vencedor(es) é(são): 2, 3')  

                # 3 jogadores vencem:
                if soma0 == soma1 and soma0 == soma2 and soma0 < soma3:
                    print('Vencedor(es) é(são): 0, 1, 2')    
                if soma0 == soma1 and soma0 == soma3 and soma0 < soma2:
                    print('Vencedor(es) é(são): 0, 1, 3')    
                if soma0 == soma2 and soma0 == soma3 and soma0 < soma1:
                    print('Vencedor(es) é(são): 0, 2, 3')    
                if soma1 == soma2 and soma1 == soma3 and soma1 < soma0:
                    print('Vencedor(es) é(são): 1, 2, 3')    

                # 4 jogadores vencem:
                if soma0 == soma1 and soma0 == soma2 and soma0 == soma3:
                    print('Vencedor(es) é(são): 0, 1, 2, 3')
                
                continua = -2
                break 
                        
    

        elif continua == -1:
            pass 
   
       


           
           
