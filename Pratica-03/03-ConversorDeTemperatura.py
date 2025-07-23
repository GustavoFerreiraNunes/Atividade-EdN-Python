print("\n3 - Conversor de Temperatura")
temperatura = float(input("Informe a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Unidade de destino (C/F/K): ").upper()

convertida = None

if origem == "C":
    if destino == "F":
        convertida = (temperatura * 9/5) + 32
    elif destino == "K":
        convertida = temperatura + 273.15
    else:
        convertida = temperatura
elif origem == "F":
    if destino == "C":
        convertida = (temperatura - 32) * 5/9
    elif destino == "K":
        convertida = ((temperatura - 32) * 5/9) + 273.15
    else:
        convertida = temperatura
elif origem == "K":
    if destino == "C":
        convertida = temperatura - 273.15
    elif destino == "F":
        convertida = ((temperatura - 273.15) * 9/5) + 32
    else:
        convertida = temperatura

if convertida is not None:
    print(f"{temperatura:.2f}°{origem} é {convertida:.2f}°{destino}")
else:
    print("Unidade inválida.")
print("-" * 40)