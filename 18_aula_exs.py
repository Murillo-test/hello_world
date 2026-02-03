# 1060

# i = 0
# contadorPOS = 0

# while (i < 6) :
#     valor = float(input())
#     if valor > 0 :
#         contadorPOS += 1
#     i += 1

# print(f"{contadorPOS} valores positivos")

# 1064

# i = 0
# contadorPOS = 0
# soma = 0

# while (i < 6) :
#     valor = float(input())
#     if valor > 0 :
#         contadorPOS += 1
#         soma += valor
#     i += 1

# media = float(soma / contadorPOS)

# print(f"{contadorPOS} valores positivos")
# print(f"{media:.1f}")

# 1066

# i = 0
# contPAR = 0
# contIM = 0
# contPOS = 0
# contNEG = 0

# while (i<5):
#     valor = int(input())
#     if (valor % 2 == 0):
#         contPAR += 1
#         if (valor > 0):
#             contPOS += 1
#         elif (valor < 0):
#             contNEG += 1
#     else:
#         contIM += 1
#         if (valor > 0):
#             contPOS += 1
#         elif (valor < 0):
#             contNEG += 1
#     i += 1

# print(f"{contPAR} valor(es) par(es)")
# print(f"{contIM} valor(es) impar(es)")
# print(f"{contPOS} valor(es) positivo(s)")
# print(f"{contNEG} valor(es) negativo(s)")

# 1067

# valor = int(input())
# i = 1

# while (i <= valor):
#     if (i % 2 != 0):
#         print(i)
#     i += 1

# 1070

# valor = int(input())
# i = 0

# while (i < 6):
#     if (valor % 2 != 0):
#         print(valor)
#         i += 1
#     valor += 1

# 1071

valX = int(input())
valY = int(input())

soma = 0

if (valX < valY):
    valX += 1
    while (valX < valY):
        if (valX % 2 != 0):
            soma += valX
        valX += 1
else:
    valY += 1
    while (valY < valX):
        if (valY % 2 != 0):
            soma += valY
        valY += 1

print(soma)