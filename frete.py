import requests
import sys
cep = input("Digite o CEP: ").strip()
cep = cep.replace("-","")

if cep.isdigit() and len(cep) == 8:
  print("Formato de CEP Válido")
else:
   print("Formato de CEP Inválido")
   sys.exit()

url = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(url)
dados = response.json()

if "erro" in dados:
  print("CEP não encontrado")
  sys.exit()
else:
  print(f"Logradouro: {dados['logradouro']}")
  print(f"Bairro: {dados['bairro']}")