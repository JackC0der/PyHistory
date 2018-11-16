def editarLinhaArquivoPorUmaChave(arquivo, chave, oQueVaiEscrever):
    arquivo1 = open(arquivo, "r")
    linhas = arquivo1.readlines()
    arquivo1.close()
    arquivo2 = open(arquivo, 'w')
    for linha in linhas:
        if chave in linha:
            arquivo2.write(linha+oQueVaiEscrever)
        else:
            arquivo2.write(linha)
    arquivo2.close()

print('''

   _a' /(   <.     Skills Creator v0.1    .>   )\ `e_
~~ _}\ \(  _  )                          (  _  )/ /{_ ~~
      \(,_(,)'                           `(.)_.)/
     ._>, _>,                             .<_ .<_. Dev Version


''')

chaveMago = "#Habilidades criadas 007689"
chaveGuerreiro = "#Habilidades criadas 00748922"
nomeDaHabilidade = input("Insira o nome da habilidade:  ")
classeDaHabilidade = input("Insira a classe da habilidade: ")
valorMinimo = int(input("Insira o valor minimo para acertar a habilidade: "))
danoMinimo = int(input("Insira o dano minimo da habilidade: "))
danoMaximo = int(input("Insira o dano maximo da habilidade: "))

habilidade = '''

    def {0}(self, dado, alvo = "sem", estadoDoJogador = "normal"):
        dano = 0
        if estadoDoJogador == "normal":
            if dado >= {1}:
                dano = random.randint({2}, {3})
            else:
                dano = 0
                return "Errou"
            if alvo != "sem":
                resultado = alvo.levarDano(dano)
                if resultado != "Morreu":
                    return alvo.nome+": -"+str(dano)+" vida. Vida atual: "+str(alvo.vida)
                else:
                    return alvo.nome+": Morre!"
            else:
                return dano
        else:
            return "Impossivel atacar! Jogador morto ou sob efeito de algo..."

'''.format(nomeDaHabilidade, valorMinimo, danoMinimo, danoMaximo)

if classeDaHabilidade.upper() == "MAGO":
    editarLinhaArquivoPorUmaChave("classes.py", chaveMago, habilidade)
if classeDaHabilidade.upper()  == "GUERREIRO":
    editarLinhaArquivoPorUmaChave("classes.py", chaveGuerreiro, habilidade)
else:
    print("Insira uma classe valida!")

#ASCII BY: http://ascii.co.uk/art/dragon