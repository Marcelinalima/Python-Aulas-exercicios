from conta import Conta
from cliente import Cliente

cliente1 = Cliente('Carlos','Rodriguez','12345678-21')
cliente2 = Cliente('Maria','Santos','78945612-36')
cliente3 = Cliente('Pedro','Silva','45612398-58')

conta1 = Conta(('123-4', 'cliente1', 1000.0, 10000.0))
conta2 = Conta(('234-8', 'cliente2',5000.0, 1000.0))
conta3 = Conta(('789-2','cliente3',8000.0, 30000.0))

conta1.deposito(1000.0)
conta1.saque(500.0)
conta2.deposito(2000.0)
conta3.deposito(1500.0)
conta3.transferencia(conta2, 800)
conta1.extrato()
conta2.extrato()
conta3.extrato()
conta1.historico.imprime()
