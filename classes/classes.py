import random
import time

from classes.monstros import *

class mago:
    def __init__(self, poderDeAtaque = 0, mana = 100):
        self.poderDeAtaque = poderDeAtaque
        self.mana = mana

    def bolaDeFogo(self, dado, alvo = "sem", estadoDoJogador = "normal"):
        if estadoDoJogador == "normal":
            dano = dado*10
            self.mana = self.mana - 10
            if alvo != "sem":
                #1* jeito automatizado de dar dano
                resultado = alvo.levarDano(dano)
                if resultado != "Morreu":
                    return alvo.nome+": -"+str(dano)+" vida. Vida atual: "+str(alvo.vida)
                else:
                    return alvo.nome+": Morre!"
            else:
                return dano
        else:
            return "Impossivel atacar! Jogador morto ou sob efeito de algo..."

    def raioCongelante(self):
        pass
    
    #Habilidades criadas 007689        

class guerreiro:
    def __init__(self, poderDeAtaque = 0, energia = 100):
        self.poderDeAtaque = poderDeAtaque
        self.energia = energia
    
    def espadaDaDiscordia(self, dado, alvo = "sem", estadoDoJogador = "normal"):
        if estadoDoJogador == "normal":
            dano = dado*10
            self.energia = self.energia - 10
            if alvo != "sem":
                #1* jeito automatizado de dar dano
                resultado = alvo.levarDano(dano)
                if resultado != "Morreu":
                    return alvo.nome+": -"+str(dano)+" vida. Vida atual: "+str(alvo.vida)
                else:
                    return alvo.nome+": Morre!"
            else:
                return dano
        else:
            return "Impossivel atacar! Jogador morto ou sob efeito de algo..."

        #Habilidades criadas 00748922
        
