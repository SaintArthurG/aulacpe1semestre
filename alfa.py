mensagem = input("Digite a mensagem: ")
chave = int(input("Digite a chave de criptografia: "))

alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

criptografado = mensagem.translate(
    str.maketrans(
        alfabeto + alfabeto_maiusculo,
        alfabeto[chave:] + alfabeto[:chave] +
        alfabeto_maiusculo[chave:] + alfabeto_maiusculo[:chave]
    )
)

print("Mensagem criptografada:", criptografado)
