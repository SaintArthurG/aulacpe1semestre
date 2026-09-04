a=input("Digite uma palavra palindroma: ")
b = a
a=a.replace(" ", "")
a= a.lower();

if (a == a[::-1]) :
    print(b);
else: 
    print("nao é um palindromo")