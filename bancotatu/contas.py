class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC Numero: {self.numero} Saldo: {self.saldo:10.2f}")

    def saque_efetuado(self, valor):
        return self.saldo >= valor

    def saque(self, valor):
        if self.saque_efetuado(valor):
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return print("Verdadeiro")
        else:
            return print("Falso")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO", valor])

    def extrato(self):
        print(f"Extrato CC N {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n     Saldo: {self.saldo:10.2f}\n")


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite=0):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def efetuar_saque(self, valor):
        return self.saldo + self.limite >= valor

    def extrato(self):
        print(f"Extrato CC N {self.numero} (Conta Especial)\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        total_disponivel = self.saldo + self.limite
        print(f"\n     Saldo: {self.saldo:10.2f}")
        print(f"     Limite: {self.limite:10.2f}")
        print(f"     Total disponível: {total_disponivel:10.2f}\n")
