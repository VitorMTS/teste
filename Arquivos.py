'''
#L9.1
arquivo=open("números.txt","w")
for linha in range(1,101):
    arquivo.write("%d\n"%linha)
arquivo.close()

#L9.2
arquivo=open("números.txt","r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

#L9.3
import sys
print("Número de parâmetros: %d" %len(sys.argv))
for n, p in enumerate(sys.argv):
    print("Parâmetro %d = %s" % (n,p))

#L9.4
ímpares=open("ímpares.txt","w")
pares=open("pares.txt","w")
for n in range(0,1000):
    if n % 2 == 0:
        pares.write("%d\n" % n)
    else:
        ímpares.write("%d\n" % n)
ímpares.close()
pares.close()

#L9.5
múltiplos4=open("múltiplos de 4.txt","w")
pares=open("pares.txt")
for l in pares.readlines():
    if int(l)%4 == 0:
        múltiplos4.write(l)
pares.close()
múltiplos4.close()

#9.3
def lê_número(arquivo):
    while True:
        número = arquivo.readline()
        # Verifica se conseguiu ler algo
        if número == "":
            return None
        # Ignora linhas em branco
        if número.strip()!="":
            return int(número)

def escreve_número(arquivo,n):
    arquivo.write("%d\n" % n);


pares = open("pares.txt","r")
ímpares = open("ímpares.txt","r")
pares_ímpares = open("pareseimpares.txt","w")
npar = lê_número(pares)
nímpar = lê_número(ímpares)
while True:
    if npar == None and nímpar == None: # Termina se ambos forem None
        break
    if npar != None and (nímpar==None or npar<=nímpar):
        escreve_número(pares_ímpares, npar)
        npar = lê_número(pares)
    if nímpar != None and (npar==None or nímpar<=npar):
        escreve_número(pares_ímpares, nímpar)
        nímpar = lê_número(ímpares)

pares_ímpares.close()
pares.close()
ímpares.close()

#9.4
import sys

# Verifica se os parâmetros foram passados
if(len(sys.argv)!=4): # Lembre-se que o nome do programa é o primeiro da lista
    print("\nUso: e09-04.py primeiro segundo saída\n\n")
else:
    primeiro = open(sys.argv[1],"r")
    segundo = open(sys.argv[2],"r")
    saída = open(sys.argv[3],"w")

    # Funciona de forma similar ao readlines
    for l1 in primeiro:
        saída.write(l1)
    for l2 in segundo:
        saída.write(l2)

    primeiro.close()
    segundo.close()
    saída.close()

#9.5
pares = open("pares.txt","r")
saída = open("pares_invertido.txt","w")

L = pares.readlines()
L.reverse()
for l in L:
    saída.write(l)

pares.close()
saída.close()

#L9.6
LARGURA=79
entrada=open("entrada.txt")
for linha in entrada.readlines():
    if linha[0]==";":
        continue
    elif linha[0]==">":
        print(linha[1:].rjust(LARGURA))
    elif linha[0]=="*":
        print(linha[1:].center(LARGURA))
    else:
        print(linha)
entrada.close

#9.6
LARGURA=79
entrada=open("entrada.txt")
for linha in entrada.readlines():
    if linha[0]==";":
        continue
    elif linha[0]==">":
        print(linha[1:].rjust(LARGURA))
    elif linha[0]=="*":
        print(linha[1:].center(LARGURA))
    elif linha[0]=="=":
        print("=" * 40)
    elif linha[0]==".":
        input("Digite algo para continuar")
        print()
    else:
        print(linha)
entrada.close()

#9.7
LARGURA = 76
LINHAS = 60
NOME_DO_ARQUIVO = "mobydick.txt"

def verifica_pagina(arquivo, linha, pagina):
    if(linha==LINHAS):
        rodapé = "= %s - Página: %d =" % (NOME_DO_ARQUIVO,pagina)
        arquivo.write(rodapé.center(LARGURA-1)+"\n")
        pagina +=1
        linha = 1
    return linha, pagina

def escreve(arquivo, linha, nlinhas, pagina):
    arquivo.write(linha+"\n")
    return verifica_pagina(arquivo, nlinhas+1, pagina)

entrada=open(NOME_DO_ARQUIVO, encoding="utf-8")
saída=open("saida_paginada.txt","w", encoding="utf-8")

pagina = 1
linhas = 1

for linha in entrada.readlines():
    palavras = linha.rstrip().split(" ")
    linha = ""
    for p in palavras:
        p=p.strip()
        if len(linha)+len(p)+1>LARGURA:
            linhas, pagina=escreve(saída, linha, linhas, pagina)
            linha = ""
        linha += p+" "
    if(linha!=""):
        linhas, pagina=escreve(saída, linha, linhas, pagina)

# Para imprimir o número na última página
while(linhas!=1):
    linhas, pagina=escreve(saída, "", linhas, pagina)

entrada.close()
saída.close()

#9.8
import sys

def verifica_pagina(arquivo, linha, pagina):
    if(linha==LINHAS):
        rodapé = "= %s - Página: %d =" % (NOME_DO_ARQUIVO,pagina)
        arquivo.write(rodapé.center(LARGURA-1)+"\n")
        pagina +=1
        linha = 1
    return linha, pagina

def escreve(arquivo, linha, nlinhas, pagina):
    arquivo.write(linha+"\n")
    return verifica_pagina(arquivo, nlinhas+1, pagina)

if len(sys.argv)!=4:
    print("\nUso: e09-08.py arquivo largura linhas\n\n")
    sys.exit(1)

NOME_DO_ARQUIVO = sys.argv[1]
LARGURA = int(sys.argv[2])
LINHAS = int(sys.argv[3])

entrada=open(NOME_DO_ARQUIVO, encoding="utf-8")
saída=open("saida_paginada.txt","w", encoding="utf-8")

pagina = 1
linhas = 1

for linha in entrada.readlines():
    palavras = linha.rstrip().split(" ")
    linha = ""
    for p in palavras:
        p=p.strip()
        if len(linha)+len(p)+1>LARGURA:
            linhas, pagina=escreve(saída, linha, linhas, pagina)
            linha = ""
        linha += p+" "
    if(linha!=""):
        linhas, pagina=escreve(saída, linha, linhas, pagina)

# Para imprimir o número na última página
while(linhas!=1):
    linhas, pagina=escreve(saída, "", linhas, pagina)

entrada.close()
saída.close()

#9.9
import sys

if len(sys.argv)<2:
    print("\nUso: e09-09.py arquivo1 [arquivo2 arquivo3 arquivoN]\n\n\n")
    sys.exit(1)

for nome in sys.argv[1:]:
    arquivo = open(nome, "r")
    for linha in arquivo:
        print(linha,end="")
    arquivo.close()

#9.10
import sys

if len(sys.argv)<2:
    print("\nUso: e09-10.py arquivo1 [arquivo2 arquivo3 arquivoN]\n\n\n")
    sys.exit(1)

saída = open("saida_unica.txt","w", encoding="utf-8")
for nome in sys.argv[1:]:
    arquivo = open(nome, "r",encoding="utf-8")
    for linha in arquivo:
        saída.write(linha)
    arquivo.close()
saída.close()

#9.11
import sys

if len(sys.argv)!=2:
    print("\nUso: e09-11.py arquivo1\n\n\n")
    sys.exit(1)

nome=sys.argv[1]
contador = {}

arquivo = open(nome, "r",encoding="utf-8")
for linha in arquivo:
    linha = linha.strip().lower()
    palavras = linha.split()
    for p in palavras:
        if p in contador:
            contador[p]+=1
        else:
            contador[p]=1
arquivo.close()

for chave in contador:
    print("%s = %d" % (chave, contador[chave] ))

#9.12
import sys

if len(sys.argv)!=2:
    print("\nUso: e09-12.py arquivo1\n\n\n")
    sys.exit(1)

nome=sys.argv[1]
contador = {}
clinha = 1
coluna = 1

arquivo = open(nome, "r",encoding="utf-8")
for linha in arquivo:
    linha = linha.strip().lower()
    palavras = linha.split(" ") # Com parâmetro considera os espaços repetidos
    for p in palavras:
        if p == "":
            coluna +=1
            continue
        if p in contador:
            contador[p].append((clinha, coluna))
        else:
            contador[p]=[ (clinha, coluna) ]
        coluna += len(p)+1
    clinha+=1
    coluna=1
arquivo.close()

for chave in contador:
    print("%s = %s" % (chave, contador[chave] ))

#9.13
import sys

# Verifica se os parâmetros foram passados
if(len(sys.argv)!=4): # Lembre-se que o nome do programa é o primeiro da lista
    print("\nUso: e09-13.py nome_do_arquivo inicio fim\n\n")
else:
    nome = sys.argv[1]
    inicio = int(sys.argv[2])
    fim = int(sys.argv[3])
    arquivo = open(nome,"r")
    for linha in arquivo.readlines()[inicio-1:fim]:
        print(linha[:-1]) # Como a linha termina com ENTER,
                          # retiramos o último caractere antes de imprimir
    arquivo.close()

#9.14
import sys

if len(sys.argv)!=3:
    print("\nUso: e09-14.py entrada saida\n\n\n")
    sys.exit(1)

entrada=sys.argv[1]
saida=sys.argv[2]


arquivo = open(entrada, "r",encoding="utf-8")
arq_saida = open(saida, "w",encoding="utf-8")
branco = 0

for linha in arquivo:
    linha = linha.rstrip() # Elimina espaços a direita
                           # Substitua por strip se também
                           #quiser eliminar espaços a esquerda
    linha = linha.replace("  ","") # Elimina espaços repetidos
    if linha=="":
        branco += 1 # Conta linhas em branco
    else:
        branco= 0 # Se a linha não está em branco, zera o contador
    if branco < 2: # Não escreve a partir da segunda linha em branco
        arq_saida.write(linha+"\n")

arquivo.close()
arq_saida.close()

#9.15
import  sys
import random

palavras = []
placar = {}

def carrega_palavras():
     arquivo = open("palavras.txt","r",encoding="utf-8")
     for palavra in arquivo.readlines():
          palavra = palavra.strip().lower()
          if palavra!="":
               palavras.append(palavra)
     arquivo.close()

def carrega_placar():
     arquivo = open("placar.txt","r",encoding="utf-8")
     for linha in arquivo.readlines():
          linha = linha.strip()
          if linha!="":
               usuario, contador = linha.split(";")
               placar[usuario]=int(contador)
     arquivo.close()

def salva_placar():
     arquivo = open("placar.txt","w",encoding="utf-8")
     for usuario in placar.keys():
          arquivo.write("%s;%d\n" %( usuario, placar[usuario] ))
     arquivo.close()

def atualize_placar(nome):
     if nome in placar:
          placar[nome]+=1
     else:
          placar[nome]=1
     salva_placar()

def exibe_placar():
     placar_ordenado = []
     for usuario, score in placar.items():
          placar_ordenado.append([usuario, score])
     placar_ordenado.sort(key = lambda score: score[1])
     print("\n\nMelhores jogadores por número de acertos:")
     placar_ordenado.reverse()
     for up in placar_ordenado:
          print("%30s %10d" % (up[0],up[1]))


carrega_palavras()
carrega_placar()

palavra = palavras[random.randint(0,len(palavras)-1)]

digitadas = []
acertos = []
erros = 0
while True:
     senha = ""
     for letra in palavra:
         senha += letra if letra in acertos else "."
     print(senha)
     if senha == palavra:
         print("Você acertou!")
         nome = input("Digite seu nome: ")
         atualize_placar(nome)
         break
     tentativa = input("\nDigite uma letra:").lower().strip()
     if tentativa in digitadas:
         print("Você já tentou esta letra!")
         continue
     else:
         digitadas += tentativa
         if tentativa in palavra:
               acertos += tentativa
         else:
               erros += 1
               print("Você errou!")
     print("X==:==\nX  :   ")
     print("X  O   " if erros >= 1 else "X")
     linha2 = ""
     if erros == 2:
         linha2 = "  |   "
     elif erros == 3:
         linha2 = " \|   "
     elif erros >= 4:
         linha2 = " \|/ "
     print("X%s" % linha2)
     linha3 = ""
     if erros == 5:
         linha3 += " /     "
     elif erros >= 6:
         linha3 += " / \ "
     print("X%s" % linha3)
     print("X\n===========")
     if erros == 6:
         print("Enforcado!")
         break

exibe_placar()
'''





















































