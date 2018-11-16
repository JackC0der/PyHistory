import classes
import monstros
import devClasses

dev = devClasses.desenvolvedor()
jogador = devClasses.player("mago", "Jack", 1, 14)
jogador.chamarClasse()
monstro = monstros.monstro("Goblin", 1)

#Cria alguns itens
dev.criarArma("Excalibur", 15)
dev.criarArmadura("ArmaduraSimples", 15)
dev.criarArmadura("ArmaduraMediana", 30)
dev.criarArmadura("ArmaduraDeAventureiro", 60)
dev.criarArmadura("Pegasus", 100)

#Define os itens de uma loja
itensDaLojaDoPrincipiante = {"ArmaduraSimples":10, "ArmaduraMediana":50, "ArmaduraDeAventureiro":100}

#Cria uma loja
dev.criarLoja("LojaDoPrincipiante", itensDaLojaDoPrincipiante)

print(dev.consultarDicionario("armadurasCriadas", "Pegasus"))

jogador.comprar("LojaDoPrincipiante", "ArmaduraSimples")
jogador.chamarClasse()
jogador.ganharNivel(1)
jogador.statusAtual()
jogador.usarItem("Excalibur")
jogador.usarItem("Pegasus")
jogador.statusAtual()

inimigoVivo = True

'''
while inimigoVivo == True:
    acao = input(">>> ")
    if acao == "atacar":
        jogador.atacar(jogador.espadaDaDiscordia, monstro)
        monstro.atacar(monstro.ataqueBasico, jogador)
'''
#Jeitos de dar dano
####Primeiro####
#Armazena o dano em uma varialvel
#dano = jogador.espadaDaDiscordia(jogador.rolarDado(jogador.nivel))
#Mostra log de batalha
#print(jogador.nick+": ataque "+str(dano))
#Aplica o dano ao alvo
#resultado = monstro.levarDano(dano)
#Mostra log de batalha
#print(monstro.nome+": "+str(resultado))
####Segundo####
#jogador.espadaDaDiscordia(jogador.rolarDado(jogador.nivel), monstro)
####Terceiro####
#jogador.atacar(jogador.espadaDaDiscordia, monstro)
