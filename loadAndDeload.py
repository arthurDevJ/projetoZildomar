import json

# Função para carregar os dados do estacionamento do arquivo JSON
def carregar_carros(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Função para salvar os dados do estacionamento no arquivo JSON
def salvar_carros(carros, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(carros, arquivo, indent=4)

# Função para adicionar um novo carro ao estacionamento
def adicionar_carro(carros, carro):
    carros.append(carro)

# Função para excluir um carro do estacionamento pelo índice
def excluir_carro(carros, indice):
    if 0 <= indice < len(carros):
        del carros[indice]
    else:
        print("Índice inválido.")

# Função para editar um carro no estacionamento pelo índice
def editar_carro(carros, indice, novo_carro):
    if 0 <= indice < len(carros):
        carros[indice] = novo_carro
    else:
        print("Índice inválido.")