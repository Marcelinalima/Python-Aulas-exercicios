# Ler os valores de entrada
A = int(input())
B = int(input())

# Verificar se são múltiplos
if A % B == 0 or B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")