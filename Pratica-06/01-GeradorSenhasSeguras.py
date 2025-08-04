import random
import string

try:
    tamanho = int(input("Digite o tamanho da senha desejada (mínimo 8): "))
    if tamanho < 8:
        print("Tamanho muito curto. Recomendado no mínimo 8 caracteres.")
    else:
        caracteres = string.ascii_letters + string.digits + "!@#$%&*"
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        print(f"Senha gerada: {senha}")
except ValueError:
    print("Entrada inválida. Digite apenas números inteiros.")
    