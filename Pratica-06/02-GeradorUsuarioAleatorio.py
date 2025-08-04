import requests

try:
    resposta = requests.get("https://www.roboform.com/br/password-generator")
    resposta.raise_for_status()  # Lança erro para status >= 400

    dados = resposta.json()
    usuario = dados["results"][0]

    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")

except requests.exceptions.RequestException as e:
    print("Erro ao acessar a API:", e)