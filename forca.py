print("Bem vindo ao jogo de forca")

palavra_secreta = "praia"
letras_acertadas = ['-','-','-','-','-']

acertou = False
enforcou = False
erros = 0

while(not acertou and not enforcou):

    chute = input('Qual letra?\n')
    if(chute in palavra_secreta):
       posicao = 0

    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_acertadas[posicao] = letra
            posicao += 1
    else:
        erros += 1  
    print(letras_acertadas) 

    enforcou = erros == 4
    acertou ='-' not in letras_acertadas

    if(acertou):
      print("voce acertou")
    else: 
      print('Voce foi enforcado')
