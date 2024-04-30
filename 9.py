def converter_real_para_euro(valor, cotacao_real_euro):
    return valor / cotacao_real_euro

def converter_real_para_dolar(valor, cotacao_real_dolar):
    return valor / cotacao_real_dolar

def converter_euro_para_dolar(valor, cotacao_euro_dolar):
    return valor * cotacao_euro_dolar

def converter_euro_para_real(valor, cotacao_real_euro):
    return valor * cotacao_real_euro

def converter_dolar_para_euro(valor, cotacao_euro_dolar):
    return valor / cotacao_euro_dolar

def converter_dolar_para_real(valor, cotacao_real_dolar):
    return valor * cotacao_real_dolar

cotacao_real_euro = float(input("Digite a cotação do Euro em relação ao Real: "))
cotacao_real_dolar = float(input("Digite a cotação do Dólar em relação ao Real: "))
cotacao_euro_dolar = float(input("Digite a cotação do Euro em relação ao Dólar: "))

print("\nMenu:")
print("1) Converter de Real para Euro")
print("2) Converter de Real para Dólar")
print("3) Converter de Euro para Dólar")
print("4) Converter de Euro para Real")
print("5) Converter de Dólar para Euro")
print("6) Converter de Dólar para Real")

opcao = int(input("\nEscolha uma opção: "))

if opcao == 1:
    valor = float(input("Digite o valor em Reais: "))
    resultado = converter_real_para_euro(valor, cotacao_real_euro)
    print("Valor em Euros:", resultado)
elif opcao == 2:
    valor = float(input("Digite o valor em Reais: "))
    resultado = converter_real_para_dolar(valor, cotacao_real_dolar)
    print("Valor em Dólares:", resultado)
elif opcao == 3:
    valor = float(input("Digite o valor em Euros: "))
    resultado = converter_euro_para_dolar(valor, cotacao_euro_dolar)
    print("Valor em Dólares:", resultado)
elif opcao == 4:
    valor = float(input("Digite o valor em Euros: "))
    resultado = converter_euro_para_real(valor, cotacao_real_euro)
    print("Valor em Reais:", resultado)
elif opcao == 5:
    valor = float(input("Digite o valor em Dólares: "))
    resultado = converter_dolar_para_euro(valor, cotacao_euro_dolar)
    print("Valor em Euros:", resultado)
elif opcao == 6:
    valor = float(input("Digite o valor em Dólares: "))
    resultado = converter_dolar_para_real(valor, cotacao_real_dolar)
    print("Valor em Reais:", resultado)
else:
    print("Opção inválida.")
