class Conta:
    def __init__(self, numero_conta, saldo=0):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.transacoes = []

    def deposito(self, valor):
        self.saldo += valor
        self.transacoes.append(("Depósito", valor))

    def saque(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            self.transacoes.append(("Saque", valor))

    def transferencia(self, outra_conta, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            outra_conta.deposito(valor)
            self.transacoes.append(("Transferência", valor, outra_conta.numero))

    def extrato(self):
        return self.transacoes


class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero):
        if numero in self.contas:
            print("Conta já existe")
        else:
            self.contas[numero] = Conta(numero)

    def deposito(self, numero_conta, valor):
        if numero_conta in self.contas:
            self.contas[numero_conta].deposito(valor)
        else:
            print("Conta não encontrada")

    def saque(self, numero_conta, valor):
        if numero_conta in self.contas:
            self.contas[numero_conta].saque(valor)
        else:
            print("Conta não encontrada")

    def transferencia(self, numero_conta_origem, numero_conta_destino, valor):
        if numero_conta_origem in self.contas and numero_conta_destino in self.contas:
            self.contas[numero_conta_origem].transferencia(self.contas[numero_conta_destino], valor)
        else:
            print("Conta não encontrada")

    def extrato(self, numero_conta):
        if numero_conta in self.contas:
            transacoes = self.contas[numero_conta].extrato()
            for transacao in transacoes:
                print(transacao)
        else:
            print("Conta não encontrada")

    def menu(self):
        while True:
            print("\n=== Menu ===")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Transferir")
            print("4. Extrato")
            print("0. Sair")

            opcao = int(input("Digite a opção desejada: "))

            if opcao == 1:
                numero_conta = input("Digite o número da conta: ")
                valor = float(input("Digite o valor do depósito: "))
                self.deposito(numero_conta, valor)

            elif opcao == 2:
                numero_conta = input("Digite o número da conta: ")
                valor = float(input("Digite o valor do saque: "))
                self.saque(numero_conta, valor)

            elif opcao == 3:
                numero_conta_origem = input("Digite o número da conta de origem: ")
                numero_conta_destino = input("Digite o número")
