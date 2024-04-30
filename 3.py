numero = float(input("Digite um número: "))

if numero > 0:
    resultado = numero * 2
    print("O dobro do número é:", resultado)
elif numero < 0:
    resultado = numero * 3
    print("O triplo do número é:", resultado)
else:
    print("O número é zero.")
