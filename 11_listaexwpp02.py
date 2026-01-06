#nome = input("Por favor, informe seu nome: ")
#print(f"Olá, {nome}!")

# ex 02

#logradouro = input("Por favor, informe o logradouro: ")
#numero = input("Certo, agora informe o número residencial: ")
#cidade = input("Por fim, informe a cidade: ")
#confirmacao = input(f"Confirma o endereço (S/N)? {logradouro}, {numero} - {cidade} : ")

# EX 03

# nome = input("Por favor, informe seu nome: ")
# idade = input("Certo. Agora informe sua idade: ")
# email = input("Por fim, informe seu e-mail: ")
# print(" ")
# print("-----------------")
# print(f"Nome: {nome}")
# print(f"Idade: {idade}")
# print(f"E-mail: {email}")
# print("-----------------")
# print(" ")

# EX 04

#nr1 = int(input("Por favor, insira o primeio número inteiro: "))
#nr2 = int(input("Agora, insira o segundo número inteiro: "))
#print(f"Soma = {nr1+nr2}")

# EX 05

#nr = int(input("Por favor, insira um número inteiro: "))
#print(f"Antecessor: {nr-1} ; Sucessor: {nr+1}")

# EX 06

#print(f"Conversor de Dias")
#dia = int(input("Por favor, insira um número de dias: "))
#print(f"O número de dias inserido equivale a {dia*24} horas ou {dia*24*60} minutos ou {dia*24*60*60} segundos.")

# EX 07

#nr = float(input("Por favor, insira um número decimal: "))
#print(f"O dobro do número inserido é: {nr*2}")

# EX 08

#nt0 = float(input("Por favor, insira a primeira nota: "))
#nt1 = float(input("Agora, insira a segunda nota: "))
#nt2 = float(input("Por fim, insira a terceira nota: "))
#md = float((nt0+nt1+nt2)/3)
#print(f"A média do aluno em questão é: {md:.2f}")

# EX 09

#cta = float(input("Por favor, insira o valor da comanda: R$ "))
#porc = float(input("Agora, insira a porcentagem de gorjeta: "))
#gorj = float(cta*(porc/100))
#tot = float(cta+gorj)
#print(f"O valor da gorjeta será de R$ {gorj:.2f} ; O valor total a pagar será de R$ {tot:.2f}.")

# EX 10

#str1 = ["arroz", "feijão", "batata"]
#print(str1)
#print(str1[0])

# EX 11

#lst1 = [ ]
#lst1.append(input("Por favor, insira a primeira fruta: "))
#lst1.append(input("Agora, insira a segunda fruta: "))
#lst1.append(input("Por fim, insira a última fruta: ")) 
#print(lst1)

# EX 12

#notas = [5.5 , 8.0 , 9.5 , 7.0]
#print(f"Maior nota: {notas[2]}")
#print(f"Menor nota: {notas[0]}")
#media = float((notas[0]+notas[1]+notas[2]+notas[3])/4)
#print(f"Média: {media:.1f}")

# EX 2 ALTERNATIVO

#end = input("Por favor, insira a rua, número e a cidade: ").split(", ")
#print(f"Endereço: Rua {end[0]}, {end[1]} - {end[2]}")

# EX 12 CORRETO

notas = [5.5, 8.0, 9.5, 7.0]
maior_nota = max(notas)  # max seleciona o maior item da lista
menor_nota = min(notas)  # min seleciona o menor item da lista

print(maior_nota)

# OU, podemos ordenar a lista com o comando .sort()

notas.sort()
maior_nota2 = notas[-1]
print(maior_nota2)

# Para fazer a média, podemos somar todos os itens
# da lista usando "sum".
# Depois, basta dividir pela quantidade de itens
# da lista. O sistema sabe o número de itens na
# lista com o comando "len" de "lenght".
# Esse comando captura o número de itens na lista.

qtd_notas = len(notas)
media = (sum(notas)/qtd_notas)
print(f"Média: {media}")
