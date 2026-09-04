import random

aleatorio = random.randint(1, 5)
entrada = input("Digite um número de 1 a 5: ")

if entrada.isdigit():
    numero = int(entrada)

    if 1 <= numero <= 5:
        if aleatorio == numero:
            print("Você acertou!")
        else:
            print("Você errou!")
    else:
        print("O número deve estar entre 1 e 5.")
else:
    print("Digite apenas números.")

print(aleatorio)
