# importando funcoes/bibliotecas de funcoes do python

from math import(sqrt) #squareroot

print(sqrt(4))

# OUTRA COISA

x = 10 # x nesse caso é uma variável global, definida para todo o código
        # se estivesse dentro da definicao de uma funcao, o valor só funcionará dentro da funcao
        # nesse caso, ele seria uma variável local

def soma(a,b):
    print(a+b*x)

soma(2,3)


# invertendo palavras

palavra = "banana"
#          012345
palavra_contrario = ""

for i in range(len(palavra)-1, -1, -1): # len captura o número de caracteres da string
    palavra_contrario += palavra[i]

print(palavra_contrario)


