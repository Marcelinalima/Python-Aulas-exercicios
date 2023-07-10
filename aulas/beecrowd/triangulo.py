    #A, B, C = [float(x) for x in input().strip().split(' ')]

    #if(A < B + C and B < A + C and C < A + B):
        #print(f"Perimetro = {(A + B + C):.1f}")
    #else:
        #print(f"Area = {((A + B)/2 * C):.1f}")


    #Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, 
    # de modo que o lado A representa o maior dos 3 lados. 
    # A seguir, determine o tipo de triângulo que estes três lados formam, 
    # om base nos seguintes casos, sempre escrevendo uma mensagem adequada:
    #se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
    #se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
    #se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
    #se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
    #se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
    #se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
    # Entrada
    #A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).
    #Saída
    #Imprima todas as classificações do triângulo especificado na entrada.

    # Ler os valores de entrada
A, B, C = sorted(map(float, input().split()), reverse=True)

# Verificar se forma um triângulo
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    # Verificar o tipo de triângulo
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    # Verificar se é equilátero ou isósceles
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
