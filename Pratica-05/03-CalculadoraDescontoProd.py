try:
    preco_original = float(input("Digite o preço original do produto (R$): "))
    desconto = float(input("Digite o percentual de desconto (ex: 20 para 20%): "))

    valor_desconto = (preco_original * desconto) / 100
    preco_final = preco_original - valor_desconto

    print(f"Preço com desconto: R$ {preco_final:.2f}")
except ValueError:
    print("Entrada inválida. Digite valores numéricos válidos.")