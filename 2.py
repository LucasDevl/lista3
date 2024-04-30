A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

soma_A_B = A + B
soma_A_C = A + C

if soma_A_B < soma_A_C:
    print("A soma de A + B é menor que A + C.")
else:
    print("A soma de A + B não é menor que A + C.")
