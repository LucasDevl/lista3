import random

def simular_dados(faces):
    return random.randint(1, faces)

def main():
    faces = int(input("Quantas faces deseja para os dados (4, 6, 8, 10, 12 ou 16)? "))

    if faces not in [4, 6, 8, 10, 12, 16]:
        print("Número de faces inválido.")
        return

    resultado = simular_dados(faces)
    print("O resultado do lançamento é:", resultado)

if __name__ == "__main__":
    main()
