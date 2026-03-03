# palavra = "IgorSergioDaSilvaManoel"
# resultado = ""

# j = 0 #primeira posição

# for i in palavra:
#     if (j != 0 and i == i.upper()):    #vejo se a letra é maiuscula e evito de um espaço ser colocado antes da primeira letra/posição da string
#         resultado+=" "
#     resultado+=i
#     j+=1

# print(resultado)


# --------------------------------------------------------------------------------------------------------------------

# remover tudo que não é número de uma lista

# lista = [5,3,2,10,66, "i", 2, "p"]
# lista_f = []
# lista_f2= []

# for i in lista:
#     if i != str(i):
#         lista_f.append(i)

# for i in lista:
#     if isinstance(i,int):
#         lista_f2.append(i)
    

# print(lista_f)

# print(lista_f2)

# lista = [5,3,2,10,66,2]

# --------------------------------------------------------------------------------------

# remover tudo que não é número de uma lista

# lista = [5,3,2,10,66, "i", 2, "p"]

# for i in lista:
#     if isinstance(i,str):
#         lista.remove(i)

# print(lista)

# --------------------------------------------------------------------------------------

# lista = [5,3,2,10,66, "i", 2, "p"]

# for i in lista:
#     if isinstance(i,str):
#         print(f"{i} foi removido da lista")
#         lista.remove(i)

# print(lista)

# -------------------------------------------------------------------------------

lista = [5,3,2,10,66, "i", 2, "p"]

cont = 0

for i in lista:
    if isinstance(i,str):
        lista.remove(i)
        lista.insert(cont,i)
        cont += 1
        

print(lista)

# lista = ["i", "p", 5, 3, 2, 10, 66, 2]