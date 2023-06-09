class Conta:
    proxima_conta_num = 1

    def __init__(self, saldo, agencia, numero_conta, senha, pessoa):
        self.saldo = saldo
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.senha = senha
        self.pessoa = pessoa


    @staticmethod
    def proxima_conta():
        numero_conta = Conta.proxima_conta_num
        Conta.proxima_conta_num += 1
        return str(numero_conta).zfill(6)

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado na conta {self.numero_conta}. Novo saldo: R${self.saldo:.2f}")
        return True

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return False
        if self.saldo < valor:
            print(f"Saldo insuficiente para saque na conta {self.numero_conta}. Saldo atual: R${self.saldo:.2f}")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado na conta {self.numero_conta}. Novo saldo: R${self.saldo:.2f}")

    def __str__(self):
        return f"Conta {self.numero_conta}\nTitular: {self.titular}\nAgência: {self.agencia}\nSaldo: R${self.saldo:.2f}"

    def extrato(self):
        return self.saldo