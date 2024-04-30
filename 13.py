def calcular_media(nota_a, nota_b):
    return (nota_a + nota_b) / 2

def verificar_aprovacao(media):
    if media >= 7.0:
        return "aprovado"
    else:
        return "recuperação"

def substituir_nota(nota_a, nota_b, escolha, nota_c):
    if escolha == 'a':
        nota_a = nota_c
    elif escolha == 'b':
        nota_b = nota_c
    return calcular_media(nota_a, nota_b)

nota_a = float(input("Digite a nota do Grau A: "))
nota_b = float(input("Digite a nota do Grau B: "))

media = calcular_media(nota_a, nota_b)
situacao = verificar_aprovacao(media)

if situacao == "aprovado":
    print("O aluno foi aprovado com média final:", media)
else:
    print("O aluno ficou em recuperação.")

    escolha = input("Deseja substituir a nota do Grau A ou do Grau B? (a/b): ").lower()

    while escolha not in ['a', 'b']:
        print("Opção inválida. Digite 'a' para substituir a nota do Grau A ou 'b' para substituir a nota do Grau B.")
        escolha = input("Deseja substituir a nota do Grau A ou do Grau B? (a/b): ").lower()

    nota_c = float(input("Digite a nota do Grau C: "))

    nova_media = substituir_nota(nota_a, nota_b, escolha, nota_c)
    nova_situacao = verificar_aprovacao(nova_media)

    if nova_situacao == "aprovado":
        print("Após a substituição, o aluno foi aprovado com média final:", nova_media)
    else:
        print("Após a substituição, o aluno foi reprovado com média final:", nova_media)
