# lista = []
# for i in range(10):
#     n = int(input())
#     if n <= 0:
#         lista.append(1)
#     else:    
#         lista.append(n)
        
# for i in range(10):
#     print(f"X[{i}] = {lista[i]}")


############################################

matriz = []

lista1 = []
lista2 = []

quad = int(input("insira numero de linhas/colunas (matriz quadrada): "))

for i in range(quad):
    n = str(input())
    lista1.append(n)
matriz.append(lista1)

print(lista1)

for j in range(quad):
    m = str(input())
    lista2.append(m)
matriz.append(lista2)

print(lista2)

for i in range(quad):
    for j in range(quad):
        print (matriz[i][j], end = "  ")
    print ()

    