import requests

cep = input("Digite o CEP (somente números): ").strip()

if not cep.isdigit() or len(cep) != 8:
    print("CEP inválido. Deve conter exatamente 8 números.")
else:
    try:
        resposta = requests.get(f"https://buscacepinter.correios.com.br/app/endereco/index.php")
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
            print(f"CEP: {dados['cep']}")

    except requests.exceptions.RequestException as e:
        print("Erro ao consultar o CEP:", e)