#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Player(object):
    def __init__(self,nome,idade):
     self.nome=nome
     self.idade=idade

class Inimigos(object):
    pass

class DragonBorn(Player):
    def __init__(self,nome,idade):
     super(DragonBorn,self).__init__(nome,idade)
     self.força=7
     self.destreza=4
     self.inteligencia=6
     vida = 100 * (self.força * 3 / 4) + 100 * (self.destreza / 2)
     self.vida = vida
     self.defesa_fisica = 10 * (self.força / 2) + 10 * (self.destreza / 3)
     self.defesa_magica = 10 * self.inteligencia
     self.pp=20.0
     self.raça='DragonBorn'

class Elfo (Player):
    def __init__(self, nome, idade):
        super(Elfo, self).__init__(nome, idade)
        self.força = 4
        self.destreza = 7
        self.inteligencia = 5
        vida = 100 * (self.força * 3/4) + 100 * (self.destreza / 2)
        self.vida = vida
        self.defesa_fisica = 10 * (self.força / 2) + 10 * (self.destreza / 3)
        self.defesa_magica = 10 * self.inteligencia
        self.pp=20.0
        self.raça='Elfo'

class Anao(Player):
    def __init__(self, nome, idade):
        super(Anao, self).__init__(nome, idade)
        self.força = 8
        self.destreza = 4
        self.inteligencia = 4
        vida = 100 * (self.força * 3 / 4) + 100 * (self.destreza / 2)
        self.vida=vida
        self.defesa_fisica=10*(self.força/2)+10*(self.destreza/3)+ 2
        self.defesa_magica=10*self.inteligencia
        self.pp=20.0
        self.raça='Anao'

class Humano(Player):
    def __init__(self,nome,idade):
     super(Humano,self).__init__(nome,idade)
     self.força=6
     self.destreza=5
     self.inteligencia=6
     vida = 100 * (self.força * 3 / 4) + 100 * (self.destreza / 2)
     self.vida = vida
     self.defesa_fisica = 10 * (self.força / 2) + 10 * (self.destreza / 3)
     self.defesa_magica = 10 * self.inteligencia
     self.pp=20.0
     self.raça='Humano'


class Esqueleto(Inimigos):
    def __init__(self):
        self.vida=300
        self.ataque=20
        self.defesa_fisica = 10
        self.defesa_magica = 15
        self.raça='Esqueleto'

    def Ataque(self,atacante, defensor):  # monstro
        defensor.vida -= (15 * atacante.ataque - 5 * defensor.defesa_magica)


class Globlin(Inimigos):
    def __init__(self):
        self.vida = 400
        self.ataque=15
        self.defesa_fisica = 15
        self.defesa_magica = 10
        self.raça='Goblin'

    def Ataque(self,atacante, defensor):  # monstro
        defensor.vida -= (15 * inimigos_dict[atacante].ataque - 5 * defensor.defesa_magica)
