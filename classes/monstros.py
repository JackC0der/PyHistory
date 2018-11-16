import random

monstro1 = '''
                         (    )
                        ((((()))
                        |o\ /o)|
                        ( (  _')
                        (._.  /\__
                        ,\___,/ '  ')
            '.,_,,       (  .- .   .    )
            \   \\     ( '        )(    )
            \   \\    \.  _.__ ____( .  |
            \  /\\   .(   .'  /\  '.  )
                \(  \\.-' ( /    \/    \)
                '  ()) _'.-|/\/\/\/\/\|
                    '\\ .( |\/\/\/\/\/|
                    '((  \    /\    /
                    ((((  '.__\/__.')
                        ((,) /   ((()   )
                        "..-,  (()("   /
                    pils  _//.   ((() ."
                _____ //,/" ___ ((( ', ___
                                ((  )
                                    / /
                                _/,/'
                                /,/,"
'''

class monstro:

    def __init__(self, nome, nivel, estado = "normal", vida = 100, arte = monstro1, dificuldade = 1):
        self.nome = nome        
        self.nivel = nivel
        self.estado = estado
        self.vida = vida
        self.arte = arte
        self.dificuldade = dificuldade

    def levarDano(self, dano):
        if self.vida - dano <= 0:
            self.estado = "Morto"
            return "Morreu"
        else:
            self.vida = self.vida - dano
            return self.vida

    def atacar(self, skill, alvo, dificuldade = 1):
        if self.estado == "normal":
            dano = skill(dificuldade)
            print(self.nome+": "+str(dano)+" de dano em "+alvo.nome)
            resultado = alvo.levarDano(dano)
            if resultado == "Morreu":
                print(alvo.nome+": Morreu")
                return "Morto"
            else:
                return "Vivo"
        else:
            print(self.nome+": Morto. Impossivel atacar")

    def ataqueBasico(self, dificuldade = 1):
        if dificuldade < 5:
            dano = random.randint(1, 5)*dificuldade
        return dano

    def ataqueComEfeito(self):
        pass