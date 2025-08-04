import unicodedata
import string

def normalizar(texto):
    texto = texto.lower()
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto)
                    if unicodedata.category(c) != 'Mn')  # remove acentos
    texto = ''.join(c for c in texto if c not in string.punctuation and not c.isspace())
    return texto

frase = input("Digite uma palavra ou frase: ")
normalizada = normalizar(frase)

if normalizada == normalizada[::-1]:
    print("Sim")
else:
    print("Não")