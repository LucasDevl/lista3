def calcular_valor_final(preco, opcao_pagamento):
    if opcao_pagamento == 1:
        return preco * 0.85  # 15% de desconto
    elif opcao_pagamento == 2:
        return preco * 0.90  # 10% de desconto
    elif opcao_pagamento == 3:
        return preco  # preço normal em duas vezes
    elif opcao_pagamento == 4:
        return preco * 1.10  # preço normal mais 10% de juros
    else:
        return None

preco_etiqueta = float(input("Digite o preço do produto: "))
opcao_pagamento = int(input("Escolha a condição de pagamento (1 - à vista em dinheiro, 2 - à vista no cartão de crédito, 3 - em duas vezes, 4 - em três vezes): "))

valor_final = calcular_valor_final(preco_etiqueta, opcao_pagamento)

if valor_final is not None:
    print("O valor final a ser pago é R$", valor_final)
else:
    print("Opção de pagamento inválida.")
