# Aula de listas
# 
# Listas são caixas com diversos
# itens. Esses itens são armazenados
# em ordem dentro de suas respectivas
# listas.

lista = ["banana", "maçã", "laranja"]

# nesse caso, banana é o item 0
# maçã é o item 1
# laranja é o item 2

print(lista) # printa a lista inteira

print(lista[0]) # pega o primeiro item da lista

# se eu quiser a última posição [-1]
# se eu quiser a penúltima posição [-2]
# e assim sucessivamente

lista.append("acerola") # ao usar o método append
                        # um novo item é adicionado à lista
print(lista)

lista[0] = "manga" # aqui estou atualizando com a palavra
                   # manga na primeira posição, em subs-
                   # tituição à palavra banana
print(lista)

lista.remove("laranja") # esse método remove item da lista
                        # pelo "valor" / identidade / string
print(lista)

lista.pop(1) # esse aqui remove o item pelo index, ou seja,
             # pelo ordenador dele
print(lista)