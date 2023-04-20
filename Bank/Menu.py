from Account import Account

class Menu:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name, balance=0):
        self.accounts[name] = Account(name, balance)
        print(f"Conta {name} criada com sucesso!")
        return self.accounts[name]

    def get_account(self, name):
        return self.accounts.get(name)

    def main_menu(self):
        while True:
            print("Bem-vindo(a) ao Banco Python!")
            print("Selecione uma opção:")
            print("1 - Criar uma nova conta")
            print("2 - Acessar uma conta existente")
            print("3 - Sair")
            choice = input("Opção selecionada: ")
            if choice == "1":
                name = input("Digite o nome do titular da conta: ")
                balance = float(input("Digite o saldo inicial da conta (opcional): "))
                self.add_account(name, balance)
            elif choice == "2":
                name = input("Digite o nome do titular da conta: ")
                account = self.get_account(name)
                if account is None:
                    print("Conta não encontrada.\n")
                    continue
                self.account_menu(account)
            elif choice == "3":
                print("Obrigado por utilizar o Banco Python. Até a próxima!")
                break
            else:
                print("Opção inválida. Tente novamente.\n")

    def account_menu(self, account):
        while True:
            print(f"Conta {account.name}")
            print("Selecione uma opção:")
            print("1 - Depositar")
            print("2 - Sacar")
            print("3 - Transferir")
            print("4 - Ver extrato")
            print("5 - Voltar ao menu principal")
            choice = input("Opção selecionada: ")
            if choice == "1":
                amount = float(input("Digite o valor a ser depositado: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Digite o valor a ser sacado: "))
                account.withdraw(amount)
            elif choice == "3":
                amount = float(input("Digite o valor a ser transferido: "))
                other_name = input("Digite o nome do titular da conta de destino: ")
                other_account = self.get_account(other_name)
                if other_account is None:
                    print("Conta de destino não encontrada.\n")
                    continue
                account.transfer(amount, other_account)
            elif choice == "4":
                account.statement()
            elif choice == "5":
                break
            else:
                print("Opção inválida. Tente novamente.\n")
