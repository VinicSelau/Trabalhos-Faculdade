class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("Depósito", amount))
        print(f"Depósito de R${amount:.2f} realizado com sucesso na conta {self.name}.")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Saldo insuficiente na conta {self.name}.")
        else:
            self.balance -= amount
            self.transactions.append(("Saque", amount))
            print(f"Saque de R${amount:.2f} realizado com sucesso na conta {self.name}.")

    def transfer(self, amount, other):
        if self.balance < amount:
            print(f"Saldo insuficiente na conta {self.name}.")
        else:
            self.balance -= amount
            self.transactions.append(("Transferência Enviada", amount))
            other.deposit(amount)
            print(
                f"Transferência de R${amount:.2f} realizada com sucesso da conta {self.name} para a conta {other.name}.")

    def statement(self):
        print(f"Extrato da conta {self.name}:")
        for transaction in self.transactions:
            print(f"{transaction[0]:<20} R${transaction[1]:.2f}")
        print(f"Saldo atual: R${self.balance:.2f}")

