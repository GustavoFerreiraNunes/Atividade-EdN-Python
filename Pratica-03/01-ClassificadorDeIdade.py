idade = int(input("1 - Informe sua idade: "))

print("\n1 - Classificador de Idade")
if idade >= 0 and idade <= 12:
    print("Categoria: Criança")
elif idade <= 17:
    print("Categoria: Adolescente")
elif idade <= 59:
    print("Categoria: Adulto")
else:
    print("Categoria: Idoso")
print("-" * 40)