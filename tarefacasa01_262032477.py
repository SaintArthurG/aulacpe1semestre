#ARTHUR HENRIQUE DOS SANTOS SOUSA ALVES DE GODOY - 262032477

import math

# Começo da parte de treinamento
print("FASE 1 - Treinamento")

# Valores iniciais dos pesos e do bias
w1 = 0.01
w2 = 0.01
b = -2.0

# Taxa usada para atualizar os pesos
eta = 0.001

# Vou usar 10 amostras para treinar o modelo
for i in range(1, 11):
    print("\nAmostra", i)

    # Entrada dos dados da pessoa
    x1 = float(input("Glicose: "))
    x2 = float(input("Idade: "))
    y = float(input("Diagnóstico real (1.0 ou 0.0): "))

    # Faz o cálculo usando os pesos atuais
    z = w1 * x1 + w2 * x2 + b

    # A sigmoide transforma o resultado em uma probabilidade
    y2 = 1 / (1 + math.exp(-z))

    # Se a probabilidade for pelo menos 50%, considero como classe 1
    if y2 >= 0.5:
        classe = 1.0
    else:
        classe = 0.0

    # Aqui vejo a diferença entre o valor real e o previsto
    erro = y - y2

    # Atualização dos pesos com base no erro
    w1 = w1 + eta * erro * x1
    w2 = w2 + eta * erro * x2
    b = b + eta * erro

    # Verifica se o modelo acertou o diagnóstico
    if classe == y:
        resultado = "ACERTO"
    else:
        resultado = "ERRO"

    print(
        "Probabilidade: {:.2f}% | Previsto: {:.1f} | Real: {:.1f} | {}".format(
            y2 * 100,
            classe,
            y,
            resultado
        )
    )

    # Mostra como ficaram os valores depois da atualização
    print(
        "Erro: {:.4f} | w1: {:.4f} | w2: {:.4f} | b: {:.4f}".format(
            erro, w1, w2, b
        )
    )


# Depois das 10 amostras, mostro os pesos que foram obtidos
print("\nTreinamento concluído.")
print(
    "Pesos finais: w1 = {:.4f} | w2 = {:.4f} | b = {:.4f}".format(
        w1, w2, b
    )
)


# Agora vou testar o modelo com uma pessoa nova
print("\nFASE 2 - Diagnóstico de novo paciente")

x1_novo = float(input("Glicose do novo paciente: "))
x2_novo = float(input("Idade do novo paciente: "))

# Uso os pesos que foram ajustados durante o treinamento
z_novo = w1 * x1_novo + w2 * x2_novo + b

# Calcula a probabilidade para o novo paciente
y_novo = 1 / (1 + math.exp(-z_novo))

# Define o diagnóstico de acordo com a probabilidade
if y_novo >= 0.5:
    diagnostico = "Alto Risco"
else:
    diagnostico = "Baixo Risco"

# Mostra o resultado final
print(
    "Probabilidade estimada: {:.3f} ({:.2f}%)".format(
        y_novo,
        y_novo * 100
    )
)

print("Diagnóstico:", diagnostico)
