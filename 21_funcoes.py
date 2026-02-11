# def define a função. Ela não é lida linearmente no código. A definição existe e só
# é colocada em ação quando chamada no código.

def calcular_preco_com_desconto(codCliente, preco):
    desconto = preco * 0.10
    preco_final = preco - desconto

    print(f"Cliente {codCliente} - Preço original R$ {preco}, Desconto: R$ {desconto}, Preço final: R$ {preco_final}")

# essa função equivale a:

# preco1 = 100
# desconto1 = preco1 * 0.10
# preco_final1 = preco1 - desconto1

# print(f"Cliente 1 - Preço original R$ {preco1}, Desconto: R$ {desconto1}, Preço final: R$ {preco_final1}")

calcular_preco_com_desconto(1, 100)

# preco2 = 300
# desconto2 = preco2 * 0.10
# preco_final2 = preco2 - desconto2

# print(f"Cliente 2 - Preço original R$ {preco2}, Desconto: R$ {desconto2}, Preço final: R$ {preco_final2}")

calcular_preco_com_desconto(2, 300)

# preco3 = 150
# desconto3 = preco3 * 0.10
# preco_final3 = preco3 - desconto3

# print(f"Cliente 3 - Preço original R$ {preco3}, Desconto: R$ {desconto3}, Preço final: R$ {preco_final3}")

calcular_preco_com_desconto(3, 150)





print("outra opção:")





def calcular_preco_com_desconto(codCliente, preco):
    desconto = preco * 0.10
    preco_final = preco - desconto

    return f"Cliente {codCliente} - Preço original R$ {preco}, Desconto: R$ {desconto}, Preço final: R$ {preco_final}"

# return faz o "retorno" do resultado, gravando ele

print(calcular_preco_com_desconto(1,100))
print(calcular_preco_com_desconto(2,300))
print(calcular_preco_com_desconto(3,150))





print("Outra opção")





def calcular_preco_com_desconto(codCliente, preco):
    desconto = preco * 0.10
    preco_final = preco - desconto

    return f"Cliente {codCliente} - Preço original R$ {preco}, Desconto: R$ {desconto}, Preço final: R$ {preco_final}"


for i in range(3):
    codCliente = input("Digite o código do cliente: ")
    preco = float(input("Digite o preco do produto: "))
    print(calcular_preco_com_desconto(codCliente,preco))

