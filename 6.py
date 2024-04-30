import random

escolha_usuario = input("Você aposta em PAR ou ÍMPAR? ").upper()

while escolha_usuario not in ['PAR', 'ÍMPAR']:
    print("Escolha inválida. Por favor, escolha entre PAR ou ÍMPAR.")
    escolha_usuario = input("Você aposta em PAR ou ÍMPAR? ").upper()

numero_usuario = int(input("Digite um número de 0 a 5: "))

while numero_usuario < 0 or numero_usuario > 5:
    print("Número inválido. Por favor, digite um número entre 0 e 5.")
    numero_usuario = int(input("Digite um número de 0 a 5: "))

numero_sorteado = random.randint(0, 5)

print("Número sorteado pelo computador:", numero_sorteado)

soma = numero_usuario + numero_sorteado

print("Soma dos números:", soma)

if (escolha_usuario == 'PAR' and soma % 2 == 0) or (escolha_usuario == 'ÍMPAR' and soma % 2 != 0):
    print("Você venceu!")
else:
    print("O programa venceu!")
