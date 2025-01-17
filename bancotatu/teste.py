from clientes import Cliente
from contas import Conta, ContaEspecial
from bancos import Banco
davy = Cliente("Davy Braga Melo Pereira", "854-236")
marisa = Cliente("Marisa Conceição", "295-102")
douglas = Cliente("Douglas Farias", "849-768")
conta1 = Conta([davy], 1, 500)
conta2 = Conta([marisa], 2, 2000)
conta3 = Conta([douglas], 10, 500)
contaDM = ContaEspecial([davy, marisa], 11, 500, 2000)
contaD = Conta([douglas], 10)
conta1.extrato()
conta2.extrato()
tatu = Banco("Tatu")
tatu.abre_conta(contaDM)
tatu.abre_conta(contaD)
tatu.lista_contas()