from Conta import Conta
from Pessoa import Pessoa

class Banco:
    proxima_agencia = 1

    def __init__(self, nome, codigo_banco):
        self.nome = nome
        self.codigo_banco = codigo_banco
        self.contas = []
        self.proxima_agencia = 1
        self.pessoas = []

    def pegar_conta(self, numero_conta, senha):
        for conta in self.contas:
            if conta.numero_conta == numero_conta and conta.senha == senha:
                return conta
        return None

    def adicionar_pessoa(self, nome, cpf, telefone, email, senha):
        agencia = str(Banco.proxima_agencia).zfill(4)
        numero_conta = str(Conta.proxima_conta()).zfill(6)
        pessoa = Pessoa(nome, cpf, telefone, email, agencia, numero_conta, senha)
        conta = Conta(0, agencia, numero_conta, senha, pessoa)

        self.pessoas.append(pessoa)
        self.contas.append(conta)

        Banco.proxima_agencia += 1

        print(f"\nConta criada com sucesso!\nAgência: {agencia}\nConta: {numero_conta}\n")

        return pessoa, agencia, numero_conta, conta

    def transferir(self, agencia_origem, numero_conta_origem, agencia_destino, numero_conta_destino, valor):
        conta_origem = self.pegar_conta(numero_conta_origem, None, agencia_origem)
        conta_destino = self.pegar_conta(numero_conta_destino, None, agencia_destino)

        if not conta_origem or not conta_destino:
            print("\nErro ao transferir: conta de origem ou destino não encontrada.")
            return False

        if conta_origem.saldo < valor:
            print("\nErro ao transferir: saldo insuficiente na conta de origem.")
            return False

        conta_origem.saldo -= valor
        conta_destino.saldo += valor

        print(f"\nTransferência de R${valor:.2f} realizada com sucesso da conta {numero_conta_origem} "
              f"da agência {agencia_origem} para a conta {numero_conta_destino} da agência {agencia_destino}.")

        return True