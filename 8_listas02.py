lista = "murillo pereira"

print(lista[0])
print(lista[1])

# para evitar que cada letra vire um item
# da lista, usar o método .split()
# o .split por padrão considera o espaço como separador

lista = "murillo pereira".split(" ")

print(lista[0])
print(lista[1])

# posso colocar um input e depois um split para separar 
# os itens inseridos no input
# lista = input().split()

