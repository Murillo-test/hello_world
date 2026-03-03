# Sequência de Fibonacci

# anterior = 0
# atual = 1
# print(anterior)
# print(atual)

# for i in range(10):
#     novo = anterior+atual
#     print(novo)
#     anterior = atual
#     atual = novo

##########################################

# def fibonacci(tam):
#     anterior = 0
#     atual = 1
    
#     for i in range(tam):
#         print(anterior)
#         novo = anterior+atual
#         anterior = atual
#         atual = novo

#########################################

# def contador_ate_10(i):
#     if i> 10:
#         return
    
#     print(i)
#     contador_ate_10(i+1)

# contador_ate_10(1)

#############################################

def fibonacci(i,n):
    cont = 0
    j = 0

    for cont in range(n):
        if i == 0:
            print(i)
            i += 1
        else:
            print(i)
            i += i
            fibonacci(i,n)

    cont += 1

fibonacci(0,10)

##############################################

# dicionario = [
#     [0,1,2],
#     [1],
#     1,
#     [3,5,6,7,8,
#         [0,1,2,3,5,6,7,8,9]]]

# def imprime_dicionario(dic, indice):
#     cont = 0

#     for item in dic:
        
#         if indice != "":
#             novo_indice = f"{indice}.{cont}"
#         else:
#             novo_indice = str(cont)

#         if (isinstance(item, int)):
#             print(f"{novo_indice}: {item}")
#         else:
#             imprime_dicionario(item, novo_indice)

#         cont +=1

# imprime_dicionario(dicionario, "")