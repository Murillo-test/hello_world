# quando quero a variável em float
# posso dividir por uma barra só ( / )
# ao invés de duas ( // )
# float é um número com vírgula

# para limitar o número de casas decimais
# do float, basta colocar o nome da variável,
# dois pontos (:), ponto (.), o número de casas
# a serem exibidas e, por fim, a letra f
# exemplo:.2f, o que vai resultar na variável
# "exemplo" com duas casas decimais

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print(f"Resultado:")
print(f"{a}x{b} = {(a*b):.2f}")
print(f"{a}+{b} = {(a+b):.2f}")
print(f"{a}-{b} = {(a-b):.2f}")
print(f"{a}/{b} = {(a/b):.2f}")