a = []
for i in range(5):
    n = int(input())
    a.append(int(n))

p = 0
im = 0
po = 0
ne = 0
for j in range(5):
    if a[j] % 2 == 0:
        p += 1
    if a[j] % 2 == 1:
        im += 1
    if a[j] > 0:
        po += 1
    if a[j] < 0:
        ne += 1
print(p, "valor(es) par(es)")
print(im, "valor(es) impar(es)")
print(po, "valor(es) positivo(s)")
print(ne, "valor(es) negativo(s)")