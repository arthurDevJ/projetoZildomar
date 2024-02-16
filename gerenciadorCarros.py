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

# Função principal
def main():
    arquivo_carros = "estacionamento.json"
    carros = carregar_carros(arquivo_carros)

    while True:
        print("\n1. Adicionar carro")
        print("2. Excluir carro")
        print("3. Editar carro")
        print("4. Mostrar carros")
        print("5. Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            marca = input("Marca do carro: ")
            modelo = input("Modelo do carro: ")
            ano = int(input("Ano do carro: "))
            vaga = input("Número da vaga: ")
            tipo_vaga = input("Tipo de vaga (normal, idoso, cadeirante): ").lower()
            novo_carro = {"marca": marca, "modelo": modelo, "ano": ano, "vaga": vaga, "tipo_vaga": tipo_vaga}
            adicionar_carro(carros, novo_carro)
            salvar_carros(carros, arquivo_carros)
            print("Carro adicionado com sucesso.")
        elif escolha == "2":
            indice = int(input("Índice do carro a ser excluído: "))
            excluir_carro(carros, indice - 1)
            salvar_carros(carros, arquivo_carros)
            print("Carro excluído com sucesso.")
        elif escolha == "3":
            indice = int(input("Índice do carro a ser editado: "))
            marca = input("Nova marca do carro: ")
            modelo = input("Novo modelo do carro: ")
            ano = int(input("Novo ano do carro: "))
            vaga = input("Novo número da vaga: ")
            tipo_vaga = input("Novo tipo de vaga (normal, idoso, cadeirante): ").lower()
            novo_carro = {"marca": marca, "modelo": modelo, "ano": ano, "vaga": vaga, "tipo_vaga": tipo_vaga}
            editar_carro(carros, indice - 1, novo_carro)
            salvar_carros(carros, arquivo_carros)
            print("Carro editado com sucesso.") 
        elif escolha == "4":
            print("\nCarros:")
            for i, carro in enumerate(carros):
                print(f"{i + 1}. {carro['marca']} {carro['modelo']} ({carro['ano']}) - Vaga: {carro['vaga']}, Tipo: {carro['tipo_vaga']}")
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
