from loadAndDeload import *

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
            marca = input("Marca do carro: ").capitalize()
            modelo = input("Modelo do carro: ").capitalize()
            ano = int(input("Ano do carro: "))
            vaga = int(input("Número da vaga: "))
            tipo_vaga = input("Tipo de vaga (normal, idoso, cadeirante): ").capitalize()
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
            marca = input("Marca do carro: ").capitalize()
            modelo = input("Modelo do carro: ").capitalize()
            ano = int(input("Ano do carro: "))
            vaga = int(input("Número da vaga: "))
            tipo_vaga = input("Tipo de vaga (normal, idoso, cadeirante): ").capitalize()
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


main()
