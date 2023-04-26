from Banco import Banco
from Conta import Conta
from Pessoa import Pessoa

class Main:

    def __init__(self):
        self.banco = Banco("Banco do Python", "001")
        self.pessoa_logada = None

    def menu_principal(self):
        while True:
            print("==== Menu Principal ====")
            print("1. Adicionar nova pessoa")
            print("2. Acessar conta")
            print("3. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionar_pessoa()
            elif opcao == "2":
                self.acessar_conta()
            elif opcao == "3":
                break
            else:
                print("Opção inválida. Tente novamente.\n")

    def adicionar_pessoa(self):
        nome = input("Digite o nome completo: ")
        cpf = input("Digite o CPF: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o e-mail: ")
        senha = input("Digite uma senha para a conta: ")

        pessoa, agencia, numero_conta, conta = self.banco.adicionar_pessoa(nome, cpf, telefone, email, senha)

        print(
            f"\nDados da nova pessoa:\nNome: {pessoa.nome}\nCPF: {pessoa.cpf}\nTelefone: {pessoa.telefone}\nE-mail: {pessoa.email}\nAgência: {agencia}\nConta: {numero_conta}\n")

    def acessar_conta(self):
        agencia = input("Digite o número da agência: ")
        numero_conta = input("Digite o número da conta: ")
        senha = input("Digite sua senha: ")

        conta = self.banco.pegar_conta(numero_conta, senha)

        if conta is None:
            print("\nConta não encontrada ou senha incorreta. Tente novamente.\n")
            return

        while True:
            print(f"\nBem-vindo(a), {conta.pessoa.nome}!")
            print("1. Ver saldo")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Transferência")
            print("5. Voltar ao menu principal")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.ver_saldo(conta)
            elif opcao == "2":
                self.depositar(conta)
            elif opcao == "3":
                self.sacar(conta)
            elif opcao == "4":
                self.transferir()
            elif opcao == "5":
                break
            else:
                print("Opção inválida. Tente novamente.\n")

    def ver_saldo(self, conta):
        saldo = conta.extrato()
        print(f"\nSaldo atual: R$ {saldo:.2f}\n")

    def depositar(self, conta):
        valor = float(input("\nValor a depositar: R$ "))
        conta.depositar(valor)
        print("\nDepósito realizado com sucesso!\n")

    def sacar(self, conta):
        valor = float(input("\nValor a sacar: R$ "))
        if conta.sacar(valor):
            print("\nSaque realizado com sucesso!\n")
        else:
            print("\nSaldo insuficiente para saque. Tente novamente.\n")

    #def transferir(self):
    #    if self.pessoa_logada:
    #        numero_conta_destino = input("Digite o número da conta de destino: ")
    #        valor = float(input("Digite o valor da transferência: "))
#
    #        conta_origem = self.banco.pegar_conta(self.pessoa_logada.numero_conta, self.pessoa_logada.senha)
    #        conta_destino = self.banco.pegar_conta(numero_conta_destino, None)
#
    #        if conta_destino:
    #            if conta_origem.saldo >= valor:
    #                conta_origem.saldo -= valor
    #                conta_destino.saldo += valor
    #                print(
    #                    f"\nTransferência realizada com sucesso!\nSaldo atual da conta {conta_origem.numero_conta}: {conta_origem.saldo}\n")
    #            else:
    #                print("\nSaldo insuficiente para realizar a transferência.\n")
    #        else:
    #            print("\nConta de destino não encontrada.\n")
    #    else:
    #        print("\nFaça o login para acessar essa opção.\n")


if __name__ == "__main__":
    app = Main()
    app.menu_principal()