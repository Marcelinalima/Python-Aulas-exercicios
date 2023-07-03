values = input().split(' ')
codigo1 = int(values[0])
quantidade1 = int(values[1])
valor1 = float(values[2])

values = input().split(' ')
codigo2 = int(values[0])
quantidade2 = int(values[1])
valor2 = float(values[2])

total = quantidade1 * valor1 + quantidade2 * valor2

print(f"VALOR A PAGAR: R$ {total:.2f}")