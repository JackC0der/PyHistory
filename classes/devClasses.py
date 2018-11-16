import random
import time

from utilitarios import *
from monstros import *
from classes import *

todosItens = {}
armasCriadas = {}
armadurasCriadas = {}
habilidadesCriadas = {}
lojasCriadas = {}

class desenvolvedor:
    def __init__(self):
        pass

    def consultarDicionario(self, dicionario, item):
        if dicionario == "armasCriadas":
            resultado = armasCriadas[item]
        elif dicionario == "armadurasCriadas":
            resultado = armadurasCriadas[item]
        elif dicionario == "habilidadesCriadas":
            resultado = habilidadesCriadas[item]
        return resultado

    def criarArma(self, nome, poderDeAtaque):
        todosItens[nome] = "arma"
        armasCriadas[nome] = int(poderDeAtaque)
        return "Arma criada com sucesso!"

    def criarArmadura(self, nome, vidaAdicional):
        todosItens[nome] = "armadura"
        armadurasCriadas[nome] = int(vidaAdicional)
        return "Armadura criada com sucesso!"

    def criarHabilidade(self, nome, classe, valorMinimoParaAcertar, danoMinimo, danoMaximo):
        habilidadesCriadas[nome] = classe

        habilidade = '''

    def {0}(self, dado, alvo = "sem", estadoDoJogador = "normal"):
        dano = 0
        if estadoDoJogador == "normal":
            if dano >= {1}:
                dano = random.randint({2}, {3})
            else:
                dano = 0
                return "Errou"
            if alvo != "sem":
                resultado = alvo.levarDano(dano)
                if resultado == "Morreu":
                    return alvo.nome+": Morre!"
                else:
                    return alvo.nome+": -"+str(dano)+" vida. Vida atual: "+str(alvo.vida)
            else:
                return dano
        else:
            return "Impossivel atacar! Jogador morto ou sob efeito de algo..."

'''.format(nome, valorMinimoParaAcertar, danoMinimo, danoMaximo)

        if classe.upper() == "MAGO":
            chave = "#Habilidades criadas 007689"
        if classe.upper() == "GUERREIRO":
            chave = "#Habilidades criadas 00748922"
        try:
            editarLinhaArquivoPorUmaChave("classes.py", chave, habilidade)
            import classes
            return "Habilidade criada com sucesso!"
        except:
            return "Falha ao criar habilidade!"

    def criarLoja(self, nome, itens):
        lojasCriadas[nome] =  itens



class player(mago, guerreiro):
    def __init__(self, classe, nome, nivel, idade, itens = [], estado = "normal", poderDeAtaque = 0, ouro = 10, vida = 100):
        self.classe = classe
        self.nome = nome
        self.nivel = nivel
        self.idade = idade
        self.itens = itens
        self.estado = estado
        self.poderDeAtaque = poderDeAtaque
        self.ouro =  ouro
        self.vida = vida

    def chamarClasse(self):
        if self.classe == "mago":
            mago.__init__(self)
            print("Chamando classe "+self.classe+"...")
            time.sleep(3)
        elif self.classe == "guerreiro":
            guerreiro.__init__(self)
            print("Chamando classe "+self.classe+"...")
            time.sleep(3)

    def rolarDado(self, dificuldade = 1):
        if self.nivel > 5:
            resultado = random.randint(5, 10) / dificuldade
        else:
            resultado = random.randint(1, 5) / dificuldade
        return resultado

    def pegarItem(self, nome):
        if todosItens[nome] == "arma":
            if nome in armasCriadas:
                self.itens.append(nome)
            else:
                return "Item nao encontrado"
        if todosItens[nome] == "armadura":
            if nome in armadurasCriadas:
                self.itens.append(nome)
            else:
                return "Item nao encontrado"

    def usarItem(self, nome):
        if todosItens[nome] == "arma":
            self.poderDeAtaque = self.poderDeAtaque + armasCriadas[nome]
            resultado = self.poderDeAtaque
        if todosItens[nome] == "armadura":
            self.vida = self.vida + armadurasCriadas[nome]
            resultado = self.vida
        return resultado

    def aumentarPoderDeAtaque(self, quantidade):
        self.poderDeAtaque = self.poderDeAtaque + quantidade
        return self.poderDeAtaque

    #2* jeito atomatizado de dar dano
    def atacar(self, skill, alvo, dificuldade = 1):
        dano = skill(self.rolarDado())
        print(self.nome+": "+str(dano)+" de dano em "+alvo.nome)
        resultado = alvo.levarDano(dano)
        if resultado == "Morreu":
            print(alvo.nome+": Morreu")
            return "Morto"
        else:
            return "Vivo"

    def ganharNivel(self, quantidade):
        self.nivel =  self.nivel+quantidade
        return self.nivel

    def statusAtual(self):
        print("Nick: "+self.nome)
        print("Nivel: "+str(self.nivel))
        print("Vida: "+str(self.vida))
        print("Poder de Ataque: "+str(self.poderDeAtaque))
        print("Ouro: "+str(self.ouro))
        
    def levarDano(self, dano):
        if self.vida - dano <= 0:
            self.estado = "Morto"
            return "Morreu"
        else:
            self.vida = self.vida - dano
            return self.vida

    def mostrarSkills(self, nivel):
        if self.classe == "mago" and nivel < 5:
            for skill in magoMenor5:
                print("Skill: "+skill)

    def comprar(self, loja, item):
        if item not in lojasCriadas[loja]:
            return "Item nao encontrado"
        itensDaLoja = lojasCriadas[loja]
        percoDoItem = itensDaLoja[item]
        if self.ouro >= percoDoItem:
            self.ouro = self.ouro - percoDoItem
            self.pegarItem(item)
        else:
            return "Ouro insuficiente"