n = int(input("Digite um numero"))
p=0
q=0
for m in range (2, n+1):
    if n%m==0:
        p=m
        q=n//m
        break
print(p)
print(q)