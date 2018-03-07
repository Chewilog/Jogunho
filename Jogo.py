#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from classes import *
from acoes import *
#Vamos gerar os inimigos
JOGAR = True
while JOGAR == True:
 inimigos=['I1', 'I2', 'I3', 'I4', 'I5']
 lista_de_inimigos=['Inimigo1', 'Inimigo2', 'Inimigo3', 'Inimigo4', 'Inimigo5']
 num_inimigos=random.randrange(1, 5)
 inimigos_dict={}
 lista_command=[]
 lista_acts=[]
 dict_acts={}
 GeraInimigos(num_inimigos,inimigos_dict)

 #Vamos criar o personagem

 print('JOGO BESTA')
 personagem = str(input('Qual personagem voce deseja criar ?(E-Elfo, D-DragonBorn, A-Anao, H-Humano)\n')).upper()
 nome_personagem = str(input('Qual o nome do seu personagem ?\n'))
 idade_personagem = int(input('Qual a idade do seu personagem?\n'))
 player,lista_acts,lista_command,dict_acts=CriaPersonagens(personagem, nome_personagem, idade_personagem)
 inimigos_dict['PL']=player
 Jogando=True
 print('Você e um %s andando na floresta quando encontra %i inimigos.'%(player.raça, num_inimigos))
 while Jogando == True:
    if player.vida == 0:
        Jogando=False
    for inimigo in inimigos:#Mostrar a vida dos inimigos a cada rodada
        if inimigo in inimigos_dict.keys():
            print ('A vida do %s é %i'%(lista_de_inimigos[inimigos.index(inimigo)],inimigos_dict[inimigo].vida))

        else:
            continue
    print('A sua vida é %i e o seu PP é %i'%(player.vida,player.pp))
    JOGADA=True
    print(lista_command)
    while JOGADA==True:
        act=input('O que voce vai fazer ? {0[0]}{1[0]} {0[1]}{1[1]} {0[2]}{1[2]} {0[3]}{1[3]}:\n'.format(lista_acts,lista_command)).upper()
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
