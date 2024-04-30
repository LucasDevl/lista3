def calcular_valor_venda(valor_compra):
    if valor_compra < 20:
        lucro = valor_compra * 0.45
    elif valor_compra <= 50:
        lucro = valor_compra * 0.35
    else:
        lucro = valor_compra * 0.25
    return valor_compra + lucro

valor_compra = float(input("Digite o valor de compra do produto: "))

valor_venda = calcular_valor_venda(valor_compra)

print("O valor de venda do produto é R$", valor_venda)

