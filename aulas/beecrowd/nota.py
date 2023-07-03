# Ler as quatro notas do aluno
N1 = float(input())
N2 = float(input())
N3 = float(input())
N4 = float(input())

# Calcular a média ponderada
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

# Exibir a média
print("Media: {:.1f}".format(media))

# Verificar a situação do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    # Ler a nota do exame
    nota_exame = float(input())
    # Exibir a nota do exame
    print("Nota do exame: {:.1f}".format(nota_exame))
    # Calcular a nova média
    nova_media = (media + nota_exame) / 2
    # Exibir a nova média
    print("Nova media: {:.1f}".format(nova_media))
    # Verificar se o aluno passou ou não com a nova média
    if nova_media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
