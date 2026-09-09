# ============================================================
# Tarefa Casa 01 - Classificador Médico Multivariado com Sigmóide
# Disciplina: Computação para Engenharia (CPE) - Turma A
# Aluno: Arthur Godoy
# Matrícula: 262032477
# ============================================================

# Importação da biblioteca math para utilizar a função exponencial
import math


# ============================================================
# FASE 1: TREINAMENTO DO MODELO
# ============================================================

print("=== FASE 1: TREINAMENTO (GLICOSE + IDADE) ===")

# Configuração inicial dos parâmetros do modelo
w1 = 0.01
w2 = 0.01
b = -2.0

# Taxa de aprendizado
eta = 0.001

# Laço de treinamento com 10 amostras
for i in range(1, 11):

    print()
    print("--- Amostra", i, "/10 ---")

    # Entrada dos dados da amostra
    x1 = float(input("Digite a glicose: "))
    x2 = float(input("Digite a idade: "))
    y = float(input("Digite o diagnóstico real (1.0 ou 0.0): "))

    # Cálculo da soma ponderada
    z = (w1 * x1) + (w2 * x2) + b

    # Cálculo da probabilidade utilizando a função sigmóide
    y_chapeu = 1 / (1 + math.exp(-z))

    # Determinação da classe prevista
    if y_chapeu >= 0.5:
        classe_prevista = 1.0
    else:
        classe_prevista = 0.0

    # Cálculo do erro
    erro = y - y_chapeu

    # Atualização dos pesos e do viés
    w1 = w1 + (eta * erro * x1)
    w2 = w2 + (eta * erro * x2)
    b = b + (eta * erro)

    # Verificação se a classificação foi correta
    if classe_prevista == y:
        status = "ACERTO"
    else:
        status = "ERRO"

    # Exibição dos resultados da amostra
    print(
        "[Saída na Tela]: Probabilidade: {:.2f} ({:.2f}%) | "
        "Classe Prevista: {:.1f} | Diagnóstico Real: {:.1f} | "
        "Status: {}".format(
            y_chapeu,
            y_chapeu * 100,
            classe_prevista,
            y,
            status
        )
    )

    print(
        "[Saída na Tela]: Erro: {:.4f} | "
        "w1: {:.4f} | w2: {:.4f} | b: {:.4f}".format(
            erro,
            w1,
            w2,
            b
        )
    )


# ============================================================
# FASE 2: RELATÓRIO DO TREINAMENTO
# ============================================================

print()
print("==================================================")
print("[Saída na Tela]: Treinamento Concluído!")
print(
    "[Saída na Tela]: Pesos Calibrados -> "
    "w1 (glicose): {:.4f} | "
    "w2 (idade): {:.4f} | "
    "b: {:.4f}".format(
        w1,
        w2,
        b
    )
)
print("==================================================")


# ============================================================
# FASE 3: DIAGNÓSTICO DE NOVO PACIENTE
# ============================================================

print()
print("=== FASE 3: DIAGNÓSTICO DE NOVO PACIENTE (INFERÊNCIA) ===")

# Solicitação dos dados do novo paciente
x1_novo = float(input("Digite a glicose do novo paciente: "))
x2_novo = float(input("Digite a idade do novo paciente: "))

# Cálculo da soma ponderada utilizando os pesos calibrados
z_novo = (w1 * x1_novo) + (w2 * x2_novo) + b

# Cálculo da probabilidade utilizando a função sigmóide
y_chapeu_novo = 1 / (1 + math.exp(-z_novo))

# Determinação do diagnóstico final
if y_chapeu_novo >= 0.5:
    diagnostico = "Alto Risco"
else:
    diagnostico = "Baixo Risco"

# Exibição da probabilidade e do diagnóstico
print(
    "[Saída na Tela]: Probabilidade Estimada: {:.3f} ({:.2f}%)".format(
        y_chapeu_novo,
        y_chapeu_novo * 100
    )
)

print("[Saída na Tela]: [DIAGNÓSTICO]:", diagnostico)
