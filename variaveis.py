# nome = input("Digite o seu nome: ")
# idade = input("Digite a sua idade: ")

# input permite ler do teclado. O comando vai
# igualar a variável ao valor digitado e vai
# permitir imprimir a variável atribuída.

# print(f"Meu nome é {nome} e eu tenho {idade} anos de idade.")

# o caractere + concatena, ou seja, ele
# apenas justapõe informações.
# Para somar de fato números, tenho
# que transformar a string em uma
# variável numérica. Posso fazer usando
# int().
# Divisão de inteiros: usar //
# Só uma / gera um número flutuante.
# Se eu quiser transformar números para
# string, posso usar a função str().

#ano_nascimento = input("Digite o ano do seu nascimento: ")
#ano_atual = int(2025)
#idade_usuario = ((ano_atual)-int(ano_nascimento))

#print(f"Você tem {idade_usuario} anos.")

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(f"Resultado:")
print(f"{a}x{b} = {a*b}")
print(f"{a}+{b} = {a+b}")
print(f"{a}-{b} = {a-b}")
print(f"{a}/{b} = {a//b}")