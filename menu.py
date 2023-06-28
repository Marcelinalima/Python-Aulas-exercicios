import forca
import adivinhacao

print ('menu de Jogos')
print('1- Adivinhacao')
print("2 - Jogo da Forca")
escolha = int(input("Qual jogo deseja jogar? Digite o numero: "))
if escolha == 1:
    adivinhacao.jogar()
elif escolha == 2 :
    forca.jogar()