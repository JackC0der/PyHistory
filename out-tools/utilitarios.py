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