# entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

#Saída
#Imprima o texto "R$" seguido de um espaço e do valor total devido de
#Imposto de Renda, com duas casas após o ponto.
#Se o valor de entrada for menor ou igual a 2000, deverá ser impressa a mensagem "Isento".
r = float(input())

if r <= 2000.00:
    i = 0
    print('Isento')
    
if 2000.00 < r <= 3000.00:
    r8 = r - 2000.00
    i = r8 * (8 / 100)
    
if 3000.00 < r <= 4500.00:
    i8 = (8 / 100) * (1000.00)
    r18 = r - 3000.00
    i = r18 * (18 / 100) + i8
    
if r > 4500.00:
    i8 = (8 / 100) * (1000.00)
    i18 = (18 / 100) * (1500.00)
    r28 = r - 4500.00
    i = i18 + i8 + r28 * (28 / 100)

if r > 2000.00:
    i = float(i)
print('R$ {:.2f}'.format(i))