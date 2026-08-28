a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
c = int(input("Digite mais um número inteiro: "))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
     b, c = c, b
print(a,b,c)