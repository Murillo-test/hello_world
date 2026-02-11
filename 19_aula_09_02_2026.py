# for é um operador "semelhante" ao while

# exemplo ex 1071 beecrowd

x = int(input())
y = int(input())

menor = x
maior = y

if (x > y):
    menor = y
    maior = x

# ou

# menor = min(x,y) -> min é um operador que determina qual o menor
# maior = max(x,y) -> max é um operador que determina o maior de uma lista

soma = 0

for i in range(x,y):  # range vai do menor número para o maior número
    if (i % 2 != 0):
        soma += 1
    
print(soma)

# for declara a variável na própria linha
# range:
    # range(5) -> começa do zero e vai até 5
    # range (5,10) -> começa de 5 e vai até 10
    # range (5,11,2) -> começa no cinco e vai até o 11 de 2 em 2

for i in range (100, 0 , -2):
    print("Comeco do for")
    print(i)
    if (i == 50):
        break # break sai do loop imediatamente, indo para "fora do loop" abaixo
    if (i == 3):
        continue # continue volta para o começo do loop
                # pulando o restante dos comandos após ele
                # ou seja, vai pular o "fim do for" e vai voltar para "comeco do for"
    print("Fim do for")

print("Fora do loop")