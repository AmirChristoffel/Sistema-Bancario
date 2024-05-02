from datetime import datetime

class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.operacoes = []
        self.saques_diarios = 0
        self.data_ultimo_saque = None

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.operacoes.append(f"Depósito de R${valor:.2f}")
            print(f"Seu saldo atual é de R${self.saldo:.2f}")
        else:
            print("Valor inválido") 

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor and valor <= 500 and self.saques_diarios < 3:
            self.saldo -= valor
            self.operacoes.append(f"Saque de R${valor:.2f}")
            self.saques_diarios += 1
            self.data_ultimo_saque = datetime.now().date()
            print(f"O saldo atual é de R${self.saldo:.2f}")
        elif self.saques_diarios >= 3:
            print("Limite diário de saques alcançado.")
        elif valor > 500:
            print("Limite máximo por saque é de R$500.")
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        print("\n--- Extrato ---")
        for operacao in self.operacoes:
            print(operacao)
        print(f"Saldo atual: R${self.saldo:.2f}")
        if self.data_ultimo_saque == datetime.now().date():
            print(f"Saques realizados hoje: {self.saques_diarios}/3")
        else:
            print("Não houve saques hoje.")

nome = input("Digite seu nome: ")
conta = ContaBancaria()
print(f"Olá, {nome}, seu saldo é de R${conta.saldo:.2f}")

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
        valor = float(input("Quanto deseja sacar? R$"))
        conta.sacar(valor)
    elif opcao == "3":
        conta.extrato()
    elif opcao == "4":
        print("Operações finalizadas.")
        break
    else:
        print("Operação inválida. Tente novamente.")
