try:
    valor_conta = float(input("Digite o valor da conta (R$): "))
    porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))

    gorjeta = (valor_conta * porcentagem) / 100
    print(f"Gorjeta: R$ {gorjeta:.2f}")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar apenas números.")