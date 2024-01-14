# Lista para armazenar os carros
estacionamento = []

# Função para adicionar um novo carro
def adicionar_carro():
    modelo = input("Digite o modelo do carro: ")
    placa = input("Digite a placa do carro: ")
    cor = input("Digite a cor do carro: ")
    carro = {'modelo': modelo, 'placa': placa, 'cor': cor}
    estacionamento.append(carro)
    print("Carro adicionado com sucesso!\n")

# Função para visualizar todos os carros
def visualizar_carros():
    if not estacionamento:
        print("Nenhum carro no estacionamento.")
    else:
        print("Lista de carros no estacionamento:")
        for i, carro in enumerate(estacionamento, start=1):
            print(f"{i}. Modelo: {carro['modelo']}, Placa: {carro['placa']}, Cor: {carro['cor']}")
        print()

# Função para atualizar informações de um carro
def atualizar_carro():
    visualizar_carros()
    if estacionamento:
        try:
            index = int(input("Digite o número do carro que deseja atualizar: ")) - 1
            if 0 <= index < len(estacionamento):
                carro = estacionamento[index]
                print(f"Atualizando informações para o carro: {carro['modelo']}, Placa: {carro['placa']}, Cor: {carro['cor']}")
                carro['modelo'] = input("Digite o novo modelo do carro: ")
                carro['placa'] = input("Digite a nova placa do carro: ")
                carro['cor'] = input("Digite a nova cor do carro: ")
                print("Informações atualizadas com sucesso!\n")
            else:
                print("Número de carro inválido.")
        except ValueError:
            print("Por favor, insira um número válido.")
    else:
        print("Não há carros para atualizar.\n")

# Função para remover um carro
def remover_carro():
    visualizar_carros()
    if estacionamento:
        try:
            index = int(input("Digite o número do carro que deseja remover: ")) - 1
            if 0 <= index < len(estacionamento):
                carro = estacionamento.pop(index)
                print(f"Carro removido: {carro['modelo']}, Placa: {carro['placa']}, Cor: {carro['cor']}\n")
            else:
                print("Número de carro inválido.")
        except ValueError:
            print("Por favor, insira um número válido.")
    else:
        print("Não há carros para remover.\n")

# Loop principal
while True:
    print("======= Sistema de Gerenciamento de Estacionamento =======")
    print("1. Adicionar Carro")
    print("2. Visualizar Carros")
    print("3. Atualizar Carro")
    print("4. Remover Carro")
    print("0. Sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        adicionar_carro()
    elif escolha == 2:
        visualizar_carros()
    elif escolha == 3:
        atualizar_carro()
    elif escolha == 4:
        remover_carro()
    elif escolha == 0:
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.\n")