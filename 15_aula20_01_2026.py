# 1015

x = input().split()
y = input().split()

x1 = float(x[0])
x2 = float(x[1])

y1 = float(y[0])
y2 = float(y[1])

distance = (((x2 - x1)**2)+((y2-y1)**2))**0.5

# 1021

valor = float(input())
total = int(round(valor*100))

qtd = total // (100*100)
print(f"{qtd} nota(s) de R$ 100.00")
total = total % (100 * 100)

qtd = total // (50*100)
print(f"{qtd} nota(s) de R$ 50.00")
total = total % (50 * 100)

qtd = total // (20*100)
print(f"{qtd} nota(s) de R$ 20.00")
total = total % (20 * 100)

qtd = total // (10*100)
print(f"{qtd} nota(s) de R$ 10.00")
total = total % (10 * 100)

qtd = total // (5*100)
print(f"{qtd} nota(s) de R$ 5.00")
total = total % (5 * 100)

qtd = total // (2*100)
print(f"{qtd} nota(s) de R$ 2.00")
total = total % (2 * 100)

# moedas

qtd = total // (1*100)
print(f"{qtd} moeda(s) de R$ 1.00")
total = total % (1 * 100)

qtd = total // (50)
print(f"{qtd} moeda(s) de R$ 0.50")
total = total % (50)

qtd = total // (25)
print(f"{qtd} moeda(s) de R$ 0.25")
total = total % (25)

qtd = total // (10)
print(f"{qtd} moeda(s) de R$ 0.10")
total = total % (10)

qtd = total // (5)
print(f"{qtd} moeda(s) de R$ 0.05")
total = total % (5)

qtd = total
print(f"{qtd} moeda(s) de R$ 0.01")
total = total % (1)