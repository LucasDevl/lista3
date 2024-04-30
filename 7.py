def calcular_desconto_previdenciario(salario):
    desconto_maximo = 318.20
    desconto_proporcional = salario * 0.11
    return min(desconto_proporcional, desconto_maximo)

salario = float(input("Digite o salário do funcionário: "))

desconto = calcular_desconto_previdenciario(salario)

print("O desconto previdenciário é de R$", desconto)
