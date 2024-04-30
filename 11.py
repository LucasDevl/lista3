def contar_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 1]
    notas_utilizadas = {}

    for cedula in cedulas:
        quantidade = valor // cedula
        if quantidade > 0:
            notas_utilizadas[cedula] = quantidade
            valor %= cedula

    return notas_utilizadas

def main():
    valor = int(input("Digite o valor para sacar: "))

    notas_utilizadas = contar_cedulas(valor)

    print("Notas utilizadas:")
    for cedula, quantidade in notas_utilizadas.items():
        print(quantidade, "nota(s) de R$", cedula)

if __name__ == "__main__":
    main()
