from datetime import datetime

class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class ContaBancaria:
    def __init__(self, cliente, agencia, num_conta):
        self.cliente = cliente
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = 0
        self.operacoes = []
        self.saques_diarios = 0
        self.data_ultimo_saque = None

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f"Depósito de R${valor:.2f}")
        print(f"Seu saldo atual é de R${self.saldo:.2f}")

    def sacar(self, valor_maximo=500):
        valor = float(input("Quanto deseja sacar? R$"))
        if self.saldo >= valor and valor <= valor_maximo and self.saques_diarios < 3:
            self.saldo -= valor
            self.operacoes.append(f"Saque de R${valor:.2f}")
            self.saques_diarios += 1
            self.data_ultimo_saque = datetime.now().date()
            print(f"O saldo atual é de R${self.saldo:.2f}")
        elif self.saques_diarios >= 3:
            print("Limite diário de saques alcançado.")
        elif valor > valor_maximo:
            print(f"Limite máximo por saque é de R${valor_maximo:.2f}.")
        else:
            print("Saldo insuficiente.")

    def extrato(self, *args, **kwargs):
        print("\n--- Extrato ---")
        for operacao in self.operacoes:
            print(operacao)
        print(f"Saldo atual: R${self.saldo:.2f}")
        if self.data_ultimo_saque == datetime.now().date():
            print(f"Saques realizados hoje: {self.saques_diarios}/3")
        else:
            print("Não houve saques hoje.")

def cadastrar_cliente():
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    data_nascimento = input("Digite sua data de nascimento (formato: DD/MM/AAAA): ")
    endereco = input("Digite seu endereço: ")
    return Cliente(nome, cpf, data_nascimento, endereco)

clientes = []
contas = []
num_conta_seq = 1

def buscar_cliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def criar_conta():
    global num_conta_seq
    cliente = cadastrar_cliente()
    cliente_existente = buscar_cliente(cliente.cpf)
    if not cliente_existente:
        clientes.append(cliente)
    conta = ContaBancaria(cliente, "0001", num_conta_seq)
    contas.append(conta)
    num_conta_seq += 1
    return conta

def lista_contas():
    print("\nComo deseja a listagem?")
    print("1. Todas as contas")
    print("2. Por CPF")
    opcao = input("Escolha a opção: ")
    if opcao == "1":
        print("\n----- Todas as Contas -----")
        for conta in contas:
            print(f"Conta: {conta.num_conta}, Cliente: {conta.cliente.nome}, Saldo: R${conta.saldo:.2f}")
    elif opcao == "2":
        cpf = input("Digite o CPF do cliente: ")
        for conta in contas:
            if conta.cliente.cpf == cpf:
                print(f"Nome: {conta.cliente.nome}, Conta: {conta.num_conta}, Saldo: R${conta.saldo:.2f}")
    else:
        print("Opção Inválida")


def selecionar_conta():
    print("Selecione sua conta bancária:")
    for conta in contas:
        print(f"{conta.num_conta}. Conta {conta.num_conta} - Agência: {conta.agencia}")
    num_conta = int(input("Digite o número da sua conta: "))
    for conta in contas:
        if conta.num_conta == num_conta:
            return conta
    print("Conta não encontrada.")
    return None

def main():
    while True:
        print("\nOpções:")
        print("1. Criar nova conta")
        print("2. Selecionar conta existente")
        print("3. Listar contas por CPF")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            conta = criar_conta()
            if conta:
                print(f"Conta criada para {conta.cliente.nome}.")
                print(f"Olá, {conta.cliente.nome}, seu saldo é de R${conta.saldo:.2f}")
                while True:
                    print("\nOpções:")
                    print("1. Depositar")
                    print("2. Sacar")
                    print("3. Extrato")
                    print("4. Sair")
                    opcao = input("Escolha uma opção: ")

                    if opcao == "1":
                        valor = float(input("Quanto deseja depositar? R$"))
                        conta.depositar(valor)
                    elif opcao == "2":
                        conta.sacar()
                    elif opcao == "3":
                        conta.extrato()
                    elif opcao == "4":
                        print("Operações finalizadas.")
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
        elif opcao == "2":
            conta = selecionar_conta()
            if conta:
                print(f"Olá, {conta.cliente.nome}, seu saldo é de R${conta.saldo:.2f}")
                while True:
                    print("\nOpções:")
                    print("1. Depositar")
                    print("2. Sacar")
                    print("3. Extrato")
                    print("4. Sair")
                    opcao = input("Escolha uma opção: ")

                    if opcao == "1":
                        valor = float(input("Quanto deseja depositar? R$"))
                        conta.depositar(valor)
                    elif opcao == "2":
                        conta.sacar()
                    elif opcao == "3":
                        conta.extrato()
                    elif opcao == "4":
                        print("Operações finalizadas.")
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
        elif opcao == "3":
            lista_contas()

        elif opcao == "4":
            print("Operações finalizadas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
