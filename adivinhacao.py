

print("Bem-vindo ao jogo da advinhação")


numero_magico = 42
pontos= 1000
rodada = 1
total_de_tentativas = 3

entrada ='invalida'

while(entrada == 'invalida'):

    nivel = input("Escolha o nivel de dificuldade\nDigite 1 para facil, 2 para médio, 3 para dificil\n")

    if nivel == '1':
        total_de_tentativas = 10
        entrada ='valida'
    elif nivel == '2':
        total_de_tentativas = 5
        entrada ='valida'
    elif nivel == '3':
        total_de_tentativas = 3
        entrada ='valida' 
    else:
        print("Entrada invalida")

#while(rodada <= total_de_tentativas):
for rodada in range(1, total_de_tentativas+1):
    print("Tentativa {} de {}". format(rodada, total_de_tentativas))
    print("Você tem {}pontos", format(pontos))

    chute = int(input("Tente adivinhar o numero magico, faça um chute \n"))
    pontos = pontos - abs(numero_magico - chute)
    if(chute == numero_magico):
        print("Acertou, voce ficou com {} pontos", format(pontos))
        break
    elif(chute > numero_magico): 
        print("Errou, chutou alto")
        if rodada == total_de_tentativas:
            print("você perdeu, 0 pontos!")

    else:
        print("Errou,chutou baixo")
        if rodada == total_de_tentativas:
            print("Você perdeu.  0 pontos!")

print ("Fim do jogo")   