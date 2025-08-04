import requests
from datetime import datetime

moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").upper()
url = f"https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiilM7t9u-OAxXrr5UCHUWgE1sQFnoECBYQAQ&url=https%3A%2F%2Fwww.bcb.gov.br%2Fconversao&usg=AOvVaw04F9gGHmWJp7XIMMOf64-G&opi=89978449"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    chave = f"{moeda}BRL"
    if chave not in dados:
        print("Código de moeda inválido.")
    else:
        info = dados[chave]
        cotacao = float(info["bid"])
        maximo = float(info["high"])
        minimo = float(info["low"])
        horario = datetime.fromtimestamp(int(info["timestamp"]))

        print(f"\nCotação {moeda}/BRL:")
        print(f"- Atual: R$ {cotacao:.2f}")
        print(f"- Máximo: R$ {maximo:.2f}")
        print(f"- Mínimo: R$ {minimo:.2f}")
        print(f"- Última atualização: {horario.strftime('%d/%m/%Y %H:%M:%S')}")

except requests.exceptions.RequestException as e:
    print("Erro ao acessar a API:", e)