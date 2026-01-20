# beecrowd 1040

# ctrl + / cria comentário de tudo

# notas = input().split()
# nt1 = float(notas[0])
# nt2 = float(notas[1])
# nt3 = float(notas[2])
# nt4 = float(notas[3])

# media = (nt1*2+nt2*3+nt3*4+nt4*1)/10

# print(f"Media: {media:.1f}")

# if media < 5.0:
#     print(f"Aluno reprovado.")
# elif media >= 7.0:
#     print(f"Aluno aprovado.")
# elif media < 7.0 and media >= 5.0:
#     print(f"Aluno em exame.")
#     exame = float(input())
#     print(f"Nota do exame: {exame:.1f}")
#     mf = (media+exame)/2
#     if mf >= 5.0:
#         print(f"Aluno aprovado.")
#     else:
#         print(f"Aluno reprovado.")
#     print(f"Media final: {mf:.1f}")




# beecrowd 1035

# entrada = input().split()
# a = int(entrada[0])
# b = int(entrada[1])
# c = int(entrada[2])
# d = int(entrada[3])

# if (b > c and d > a and (c+d)>(a+b) and c>0 and d>0 and a%2==0):   # "%" pega o "resto" de uma divisão. Ex: Se 5 / 2 = 2,5, então 5 % 2 = 0,5.
#                                                                     # Ou seja, se o resto de uma divisão por 2 for igual a zero, o número é par.
#     print(f"Valores aceitos")
# else:
#     print(f"Valores nao aceitos")




# 1050

# entrada = input()
# dicionario = {
#     "61": "Brasilia",
#     "71": "Salvador",
#     "11": "Sao Paulo",
#     "21": "Rio de Janeiro",
#     "32": "Juiz de Fora",
#     "19": "Campinas",
#     "27": "Vitoria",
#     "31": "Belo Horizonte",
# }

# if dicionario.get(entrada) == None:
#     print("DDD nao cadastrado")
# else:
#     print(dicionario.get(entrada))
