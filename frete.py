import requests

def valida_cep(cep):
  cep = cep.replace("-","").strip()
  if cep.isdigit() and len(cep) == 8:
    return True
  else:
    return False

def consulta_cep(cep):
  url = f"https://viacep.com.br/ws/{cep}/json/"
  response = requests.get(url)
  dados = response.json()
  if "erro" in dados:
    return None
  else:
    return dados


while True:
  cep = input("Digite o CEP: ").strip()
  if valida_cep(cep):
    dados = consulta_cep(cep)
    if dados is None:
      print("CEP não encontrado")
    else:
      print(f"Logradouro: {dados['logradouro']}")
      print(f"Bairro: {dados['bairro']}")
      opcao = input("\n Digite 0 para nova consulta (outra tecla para sair)")

      if opcao != "0":
        print("Encerrando...")
        break
  else:
    print("Formato de CEP inválido")