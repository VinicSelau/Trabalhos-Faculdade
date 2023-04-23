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

        return pessoa, agencia, numero_conta
