peso = float(input("2 - Informe seu peso (kg): "))
altura = float(input("2 - Informe sua altura (m): "))
imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print("\n2 - Calculadora de IMC")
print(f"Peso: {peso:.2f} kg")
print(f"Altura: {altura:.2f} m")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")
print("-" * 40)