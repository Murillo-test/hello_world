# Criar funcao chamada palindromo passando uma string e retorna True ou False se a palavra é igual de tras pra frente

palavra = input("Insira uma palavra para determinar se ela é um palíndromo: ")

def palindromo(palavra):
    palavra_contrario = ""
    for i in range(len(palavra)-1, -1, -1): 
        palavra_contrario += palavra[i]
    return palavra == palavra_contrario

if palindromo(palavra):     # como armazenei um valor true ou false através do return (comparação entre duas strings)
                            # e o if só roda no true, jogo if para true e else para falso
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")



# palavra = "banana"
# #          012345
# palavra_contrario = ""

# for i in range(len(palavra)-1, -1, -1): # len captura o número de caracteres da string
#     palavra_contrario += palavra[i]

# print(palavra_contrario)
