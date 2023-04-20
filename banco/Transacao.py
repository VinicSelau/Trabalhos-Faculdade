from datetime import datetime

class Transacao:
    def __init__(self, tipo, valor, origem=None, destino=None):
        self.tipo = tipo
        self.valor = valor
        self.origem = origem
        self.destino = destino
        self.data = datetime.now()

    def __str__(self):
        if self.tipo == "Depósito":
            return f"{self.tipo} de R${self.valor:.2f} na conta {self.destino} em {self.data.strftime('%d/%m/%Y %H:%M:%S')}"
        elif self.tipo == "Saque":
            return f"{self.tipo} de R${self.valor:.2f} na conta {self.origem} em {self.data.strftime('%d/%m/%Y %H:%M:%S')}"
        else:
            return f"{self.tipo} de R${self.valor:.2f} da conta {self.origem} para a conta {self.destino} em {self.data.strftime('%d/%m/%Y %H:%M:%S')}"
