arquivo1 = open("arquivo1.txt", "wt")
conteudo1 = "Um texto qualquer"
arquivo1.write(conteudo1)
arquivo1.close()

arquivo1 = open("arquivo1.txt", "r")
conteudo = arquivo1.read()

print(conteudo)
arquivo1.close()