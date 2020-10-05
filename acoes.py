#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from classes import *
def GeraInimigos (num_inimigos,inimigos_dict):#Funçao que gera inimigos
   inimigos=['I1','I2','I3','I4','I5']
   for cria_inimigo in range (num_inimigos) :
       if random.randrange(2)==0:
        cria_inimigo= inimigos[cria_inimigo]
        inimigos_dict[cria_inimigo] = Esqueleto()
       else:
        cria_inimigo = inimigos[cria_inimigo]
        inimigos_dict[cria_inimigo] = Globlin()
   return num_inimigos,inimigos_dict
def PararJogo ():
    return False




#MONSTROS
def ataca_player (key,player,inimigos_dict):
    Ataque1(key,player,inimigos_dict)


def Ataque1(key, player,inimigos_dict):  # monstro
    player.vida -= (15 * inimigos_dict[key].ataque - 5 * player.defesa_magica)/(len(inimigos_dict.keys())-1)

#TODOS
def Pass():#todos(passa a rodada)
    JOGADA=False
    return JOGADA

#ELFO
def Apunhalada(atacante,defensor,inimigos_dict):#elfo
    custopp = 1
    if atacante.pp-custopp<0:
        print('Voce nao tem PP suficiente')
        JOGADA=True
        return JOGADA
    else:
     atacante.pp -= custopp
     inimigos_dict[defensor].vida -= ((12 * atacante.força/3 + 20 * atacante.destreza) - (8 * inimigos_dict[defensor].defesa_fisica))
     JOGADA=False
     return  JOGADA

def Flechada(atacante,defensor,inimigos_dict):#elfo
    custopp = 2
    if atacante.pp - custopp < 0:
        print('Voce nao tem PP suficiente')
        JOGADA = True
        return JOGADA
    else:
     atacante.pp-=custopp
     inimigos_dict[defensor].vida -= (10*atacante.força/2 + 20*atacante.destreza - 5*inimigos_dict[defensor].defesa_fisica)
     JOGADA=False
     return JOGADA

def FlechaEspecial(atacante,defensor,inimigos_dict):#elfo
    custopp = 4
    if atacante.pp - custopp < 0:
        print('Voce nao tem PP suficiente')
        JOGADA = True
        return JOGADA
    else:
     atacante.pp-= custopp
     inimigos_dict[defensor].vida -= (12*atacante.força/3+20*atacante.destreza + 12*atacante.inteligencia - (8*inimigos_dict[defensor].defesa_fisica + 5*inimigos_dict[defensor].defesa_magica))
     JOGADA=False
     return JOGADA

#ANAO
def Martelada(atacante,defensor,inimigos_dict):#anao
    custopp = 1
    if atacante.pp - custopp < 0:
        print('Voce nao tem PP suficiente')
        JOGADA = True
        return JOGADA
    else:
     atacante.pp-=custopp
     inimigos_dict[defensor].vida -= ((10 * atacante.força + 10 * atacante.destreza/2) - (5 * inimigos_dict[defensor].defesa_fisica))
     JOGADA=False
     return   JOGADA

def Rage(conjurador,alvo,inimigos_dict):#anao////cria funçao especial
    custopp = 4
    if conjurador.pp - custopp < 0:
        print('Voce nao tem PP suficiente')
        JOGADA = True
        return JOGADA
    else:
     conjurador.pp -= custopp
     inimigos_dict[alvo].força+=2
     JOGADA=False
     return JOGADA

def GolpeGiratorio(atacante,defensor,inimigos_dict):#anao
    custopp = 3
    if atacante.pp - custopp < 0:
        print('Voce nao tem PP suficiente')
        JOGADA = True
        return JOGADA
    else:
     atacante.pp-=custopp
     inimigos_dict[defensor].vida -= ((14 * atacante.força + 10 * atacante.destreza / 2) - (7 * inimigos_dict[defensor].defesa_fisica))
     JOGADA=False
     return JOGADA

#DRAGONBORN
def Espadada(atacante,defensor,inimigos_dict):#dragonborn
    custopp = 1
    if atacante.pp - custopp < 0:
        print('Voce nao tem PP suficiente')
        JOGADA = True
        return JOGADA
    else:
        atacante.pp -= custopp
        inimigos_dict[defensor].vida -= ((10 * atacante.força * 3/4 + 10 * atacante.destreza/2) - (5*inimigos_dict[defensor].defesa_fisica))
        JOGADA=False
        return JOGADA

def Shout(atacante,defensor,inimigos_dict):#dragonborn
    custopp = 2
    if atacante.pp - custopp < 0:
        print('Voce nao tem PP suficiente')
        JOGADA = True
        return JOGADA
    else:
        atacante.pp -= custopp
        inimigos_dict[defensor].vida -= ((17 * atacante.inteligencia) - (5 * inimigos_dict[defensor].defesa_magica))
        JOGADA=False
        return JOGADA
def FuriaDoDragao (atacante,defensor,inimigos_dict):#dragonborn
    custopp = 4
    if atacante.pp - custopp < 0:
        print('Voce nao tem PP suficiente')
        JOGADA = True
        return JOGADA
    else:
        atacante.pp -= custopp
        inimigos_dict[defensor].vida -= ((20 * (atacante.força + atacante.inteligencia))-(5*(inimigos_dict[defensor].defesa_magica + inimigos_dict[defensor].defesa_fisica)))
        JOGADA = False
        return JOGADA

#HUMANO
def AvançaEscudo(atacante,defensor,inimigos_dict):#humano
    custopp = 1
    if atacante.pp - custopp < 0:
        print('Voce nao tem PP suficiente')
        JOGADA = True
        return JOGADA
    else:
        atacante.pp -= custopp
        inimigos_dict[defensor].vida -= ((10 * atacante.força + 10 * atacante.destreza * 2/5) - (5 * inimigos_dict[defensor].defesa_fisica))
        JOGADA=False
        return JOGADA

def Curar(conjurador,alvo,inimigos_dict):#humano///funçao especial
    custopp = 3
    if conjurador.pp - custopp < 0:
        print('Voce nao tem PP suficiente')
        JOGADA = True
        return JOGADA
    else:
        conjurador.pp -= custopp
        a=50
        if ((100 * (conjurador.força * 3 / 4) + 100 * (conjurador.destreza / 2)) - conjurador.vida) > a :
            alvo.vida += ((100 * (conjurador.força * 3 / 4) + 100 * (conjurador.destreza / 2)) - conjurador.vida)
        else:
            inimigos_dict[alvo].vida += a

def EspadaDeFogo(atacante,defensor,inimigos_dict):#humano
    custopp = 4
    if atacante.pp - custopp < 0:
        print('Voce nao tem PP suficiente')
        JOGADA = True
        return JOGADA
    else:
        atacante.pp -= custopp
        inimigos_dict[defensor].vida -= ((17 * (atacante.força + atacante.magica)) - (5 * (inimigos_dict[defensor].defesa_magica + inimigos_dict[defensor].defesa_fisica)))
        JOGADA=False
        return JOGADA
def CriaPersonagens(personagem,nome_personagem,idade_personagem):#Funçao que cria o player
    if personagem in ('E', 'ELFO'):
        lista_acts = ['Apunhalada(PP-1)', 'Flechada(PP-2)', 'Flecha.Esp(PP-4)', 'Pass(Sem custo)']
        lista_command=['A','F','FE','P']
        elfo_acts_dict = {'A': Apunhalada, 'F': Flechada, 'FE': FlechaEspecial,
                          'P': Pass()}
        return Elfo(nome_personagem, idade_personagem),lista_acts,lista_command,elfo_acts_dict
    elif personagem in ('D', 'DRAGONBORN'):
        lista_acts = ['Espadada(PP-1)', 'Shout(PP-2)', 'FuriaDoDragao(PP-4)', 'Pass(Sem custo)']
        lista_command =['E','S','FD','P']
        db_acts_dict = {'E': Espadada, 'S': Shout, 'FD': FuriaDoDragao, 'P': Pass}
        return DragonBorn(nome_personagem, idade_personagem),lista_acts,lista_command,db_acts_dict
    elif personagem in ('A', 'ANAO'):
        lista_acts = ['Martelada(PP-1)', 'Rage(PP-4)', 'GolpeGiratório(PP-3)', 'Pass(Sem custo)']
        lista_command =['M','R','GG','P']
        anao_acts_dict = {'M': Martelada, 'R': Rage, 'GG': GolpeGiratorio, 'P': Pass}
        return Anao(nome_personagem, idade_personagem),lista_acts,lista_command,anao_acts_dict
    else:
        lista_acts = ['AvançoEscudo(PP-1)', 'Curar(PP-3)', 'EspadaDeFogo(PP-4)', 'Pass(Sem custo)']
        lista_command =['AE','C','EF','P']
        humano_acts_dict = {'AE': AvançaEscudo, 'C': Curar, 'EF': EspadaDeFogo,
                            'P': Pass}
        return Humano(nome_personagem, idade_personagem),lista_acts,lista_command,humano_acts_dict




