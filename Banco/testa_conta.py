from conta import Conta
from cliente import Cliente


cliente = Cliente('Marcelina' , 'Pires', '12345678-00')
cliente1 = Cliente('Alice' , 'Alves', '12345678-00')

conta = Conta('123-4', cliente, 1000.0, 10000.0)
conta1 = Conta('321-4', cliente1, 500.0, 10000.0)

conta1.depositar(250.0)
conta1.extrato()
conta1.sacar(500.0)
conta1.tranferir(conta,200.0)
conta.extrato()
conta1.extrato()
