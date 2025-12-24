from entidades.cliente import Cliente
from entidades.conta import Conta, ContaCorrente, ContaPoupanca
from utilitarios.exceptions import ContaInexistenteError

class Banco:
    def __init__(self, nome: str):
        self.nome = nome
        self._clientes = {}
        self._contas = {}

    def adicionar_cliente(self, nome:str, cpf: str):
        if cpf in self._clientes:
            print('Erro: Já existe um cliente com este CPF!')
            return self._clientes[cpf]
        
        novo_cliente = Cliente(nome, cpf)
        self._clientes[cpf] = novo_cliente

        print(f'Cliente {nome} adicionado com sucesso!')

        return novo_cliente
    
    def criar_conta(self, cliente: Cliente, tipo: str) -> Conta:
        numero_conta = Conta.get_total_contas() + 1

        if tipo.lower() == 'corrente':
            nova_conta = ContaCorrente(numero_conta, cliente)

        elif tipo.lower() == 'poupanca':
            nova_conta = ContaPoupanca(numero_conta, cliente)

        else:
            print('Tipo de conta inválido. Escolha "corrente" ou "poupanca".')
            return None
        
    def buscar_conta(self, numero_conta: int) -> Conta:
        conta = self._contas.get(numero_conta)

        if not conta:
            raise ContaInexistenteError(numero_conta)
        return conta