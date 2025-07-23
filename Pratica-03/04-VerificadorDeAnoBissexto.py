# 4 - Verificador de Ano Bissexto
ano = int(input("4 - Informe um ano: "))

print("\n4 - Verificador de Ano Bissexto")
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
print("-" * 40)