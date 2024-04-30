def calcular_valor_plano(idade, dependentes):
    valor_base = 300
    valor_dependentes = 0

    for dependente_idade in dependentes:
        if dependente_idade < 10:
            valor_dependentes += 100
        elif 10 <= dependente_idade <= 30:
            valor_dependentes += 220
        elif 31 <= dependente_idade <= 60:
            valor_dependentes += 395
        else:
            valor_dependentes += 480

    return valor_base + valor_dependentes

idade_conveniado = int(input("Digite a idade do conveniado: "))
quantidade_dependentes = int(input("Digite a quantidade de dependentes: "))

idades_dependentes = []
for i in range(quantidade_dependentes):
    idade_dependente = int(input("Digite a idade do dependente {}: ".format(i + 1)))
    idades_dependentes.append(idade_dependente)

valor_total = calcular_valor_plano(idade_conveniado, idades_dependentes)

print("O valor total a ser pago pelo plano de saúde é de R$", valor_total)
