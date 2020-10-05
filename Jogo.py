#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from classes import *
from acoes import *
#Vamos gerar os inimigos
JOGAR = True
while JOGAR == True:
 inimigos=['I1', 'I2', 'I3', 'I4', 'I5']
 lista_de_inimigos=['Inimigo-1', 'Inimigo-2', 'Inimigo-3', 'Inimigo-4', 'Inimigo-5']
 num_inimigos=random.randrange(1, 5)
 inimigos_dict={}
 lista_command=[]
 lista_acts=[]
 dict_acts={}
 GeraInimigos(num_inimigos,inimigos_dict)

 #Vamos criar o personagem

 print('JOGO SUPIMPA')
 personagem = str(input('Qual personagem voce deseja criar ?\n[E]-Elfo(a)\n[D]-DragonBorn\n[A]-Anao(ã)\n[H]-Humano(a)\n')).upper()
 nome_personagem = str(input('Qual o nome do seu personagem ?\n'))
 idade_personagem = int(input('Qual a idade do seu personagem?\n'))
 player,lista_acts,lista_command,dict_acts=CriaPersonagens(personagem, nome_personagem, idade_personagem)
 inimigos_dict['PL']=player
 Jogando=True
 print('Você e um %s andando na floresta quando encontra %i inimigos.'%(player.raça, num_inimigos))
 while Jogando == True:
    if player.vida == 0:
        Jogando=False
    # print('\n')
    for inimigo in inimigos:#Mostrar a vida dos inimigos a cada rodada
        if inimigo in inimigos_dict.keys():
            print ('A vida do %s é %i'%(lista_de_inimigos[inimigos.index(inimigo)],inimigos_dict[inimigo].vida))

        else:
            continue
    print('\nA sua vida é %i e o seu PP é %i'%(player.vida,player.pp))
    JOGADA=True
    # print(lista_command)
    while JOGADA==True:
        act=input('O que voce vai fazer ? \n[{1[0]}]-{0[0]} \n[{1[1]}]-{0[1]} \n[{1[2]}]-{0[2]} \n[{1[3]}]-{0[3]}:\n'.format(lista_acts,lista_command)).upper()
        print('Quem voce quer atacar ?:')
        for inimig in inimigos_dict.keys():
            print(inimig)
        print ('Player |Pl' )
        alvo=input().upper()
        if alvo in ('PL'):
            dict_acts[act](player, player,inimigos_dict)
        if act in lista_command:
            dict_acts[act](player,alvo,inimigos_dict)
            break
        else:
            print('Entrada Invalida')
    #Termina Jogada
    copia_dict=inimigos_dict.copy()
    for inimigo in copia_dict.keys():
        if inimigos_dict[inimigo].vida<=0:
                print('voce matou',inimigo)
                del(inimigos_dict[inimigo])
    if len(inimigos_dict.keys())==0:
        print('VOCE GANHOU!!!')
        break
    for key in inimigos_dict.keys():#vai chamar a funçao para atacar
        if key=='PL':
            continue
        ataca_player(key,player,inimigos_dict)

    if player.vida<=0:
            print('VOCE PERDEU!!!')
            break
    if player.pp<4:
            player.pp+=0.5

 continuar=input('Voce quer jogar denovo (S-SIM|N-NAO):').upper()
 if continuar in ('S','SIM'):#Caso sim vai reiniciar o ciclo de jogar
    Jogando=False
 else:
    exit()
