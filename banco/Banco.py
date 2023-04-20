from Conta import Conta
from Transacao import Transacao

class Banco:
    def __init__(self):
        self.contas = []

    def criar_conta(self, numero_conta):
        self.contas.append(Conta(numero_conta))

    def encontrar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        return None

    def deposito(self, numero_conta, valor):
        conta = self.encontrar_conta(numero_conta)
        if conta:
            conta.deposito(valor)
            transacao = Transacao("Depósito", valor, destino=numero_conta)
            print(transacao)
        else:
            print("Conta não encontrada.")

    def saque(self, numero_conta, valor):
        conta = self.encontrar_conta(numero_conta)
        if conta:
            conta.saque(valor)
            transacao = Transacao("Saque", valor, origem=numero_conta)
            print(transacao)
        else:
            print("Conta não encontrada.")

    def transferencia(self, origem, destino, valor):
        conta_origem = self.encontrar_conta(origem)
        conta_destino = self.encontrar_conta(destino)
        if conta_origem and conta_destino:
            conta_origem.saque(valor)
            conta_destino.deposito(valor)
            transacao = Transacao("Transferência", valor, origem=origem, destino=destino)
            print(transacao)
        else:
            print("Conta(s) não encontrada(s).")

    def extrato(self, numero_conta):
        conta = self.buscar_conta(numero_conta)

        if conta:
            print(f"Extrato da conta {numero_conta}:")
            for transacao in conta.transacoes:
                print(transacao)
        else:
            print("Conta não encontrada.")

    def menu(self):
        while True:
            print("Selecione uma opção:")
            print("1 - Depositar")
            print("2 - Sacar")
            print("3 - Transferir")
            print("4 - Extrato")
            print("0 - Sair")
            opcao = input("=> ")

            if opcao == "1":
                numero_conta = input("Digite o número da conta: ")
                valor = float(input("Digite o valor do depósito: "))
                self.deposito(numero_conta, valor)
            elif opcao == "2":
                numero_conta = input("Digite o número da conta: ")
                valor = float(input("Digite o valor do saque: "))
                self.saque(numero_conta, valor)
            elif opcao == "3":
                origem = input("Digite o número da conta de origem: ")
                destino = input("Digite o número da conta de destino: ")
                valor = float(input("Digite o valor da transferência: "))
                self.transferencia(origem, destino, valor)
            elif opcao == "4":
                numero_conta = input("Digite o número da conta: ")
                self.extrato(numero_conta)
            else:
                print("Opção inválida.")
