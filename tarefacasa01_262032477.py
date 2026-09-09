import math

print("FASE 1 - Treinamento")

w1 = 0.01
w2 = 0.01
b = -2.0
eta = 0.001

for i in range(1, 11):
    print("\nAmostra", i)

    x1 = float(input("Glicose: "))
    x2 = float(input("Idade: "))
    y = float(input("Diagnóstico real (1.0 ou 0.0): "))

    z = w1 * x1 + w2 * x2 + b

    y_chapeu = 1 / (1 + math.exp(-z))

    if y_chapeu >= 0.5:
        classe = 1.0
    else:
        classe = 0.0

    erro = y - y_chapeu

    w1 = w1 + eta * erro * x1
    w2 = w2 + eta * erro * x2
    b = b + eta * erro

    if classe == y:
        resultado = "ACERTO"
    else:
        resultado = "ERRO"

    print(
        "Probabilidade: {:.2f}% | Previsto: {:.1f} | Real: {:.1f} | {}".format(
            y_chapeu * 100,
            classe,
            y,
            resultado
        )
    )

    print(
        "Erro: {:.4f} | w1: {:.4f} | w2: {:.4f} | b: {:.4f}".format(
            erro, w1, w2, b
        )
    )


print("\nTreinamento concluído.")
print(
    "Pesos finais: w1 = {:.4f} | w2 = {:.4f} | b = {:.4f}".format(
        w1, w2, b
    )
)


print("\nFASE 2 - Diagnóstico de novo paciente")

x1_novo = float(input("Glicose do novo paciente: "))
x2_novo = float(input("Idade do novo paciente: "))

z_novo = w1 * x1_novo + w2 * x2_novo + b

y_novo = 1 / (1 + math.exp(-z_novo))

if y_novo >= 0.5:
    diagnostico = "Alto Risco"
else:
    diagnostico = "Baixo Risco"

print(
    "Probabilidade estimada: {:.3f} ({:.2f}%)".format(
        y_novo,
        y_novo * 100
    )
)

print("Diagnóstico:", diagnostico)
