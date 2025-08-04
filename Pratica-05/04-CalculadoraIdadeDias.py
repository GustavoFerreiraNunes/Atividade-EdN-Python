from datetime import datetime

try:
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = datetime.now().year

    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # desconsiderando anos bissextos

    print(f"Idade aproximada em dias: {idade_dias} dias")
except ValueError:
    print("Entrada inválida. Digite um ano válido.")