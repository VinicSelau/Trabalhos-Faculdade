class Conta:
    proxima_conta_num = 1

    class Conta:
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
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def extrato(self):
        return self.saldo