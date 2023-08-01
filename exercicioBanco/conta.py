
from cliente import Cliente
from historico import Historico

class Conta:
    _total_de_contas : 1

    def __init__(self, cliente, numero, saldo):
        print('Inicializando a conta')
        self._titular = cliente.nome
        self._numero = numero
        self._saldo = 0
        self.historico = Historico()
       
        Conta.total_de_contas  += 1

    @property
    def historico(self):
        return self._historico

    @staticmethod
    def get_total_de_contas():
        return Conta._total_de_contas0
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def numero(self):
        return self.numero
    
    @property
    def saldo(self):
        return self._saldo
    

    def depositar(self, valor):
        self._saldo += valor
        self.historico.transacoes.append("Depósito de {} reais".format(valor))

    def saque(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {} reais".format(valor))
            return True
        
    def extrato(self):
        print("numero: {} \ntitular: {} \nsaldo: {}".format(self.numero, self.titular, self.saldo))
        self.historico.transacoes.append("tirou o extrato - saldo {} reais".format(self.saldo))

    def transferencia(self, conta_destino, valor):
        retirada = self.sacar(valor)
        if (retirada == False):
            return False
        else:
            conta_destino.depositar(valor)
            self.historico.transacoes.append("envio de {} reais sacados para a conta {}".format(valor, conta_destino.numero))
            return True

    
