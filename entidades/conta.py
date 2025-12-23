from abc import ABC, abstractclassmethod
from datetime import datetime
'''from utilitarios.exceptions import SaldoInsuficienteError'''

class Conta:
    _total_contas=0
    def __init__(self, numero: int, cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0
        self._historico = []

        Conta._total_contas += 1

    @property
    def saldo(self):
        return self._saldo 
    
    @classmethod
    def get_total_contas(cls):
        return cls._total_contas 
    
    def depositar(self, valor: float):
        if valor>0:
            self._saldo += valor
            self._historico.append((datetime.now(), f"Depósito de R${valor:.2f}"))
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")

        else:
            print('Valor de depósito inválido!')

    @abstractclassmethod
    def sacar(self, valor: float):
        pass

    def extratro(self):
        print(f'\n---Extrato da conta N° {self._numero} ---')
        print(f'Cliente: {self._cliente.nome}')
        print(f'Saldo atual: R${self.saldo:.2f}')
        print('Histórico de transações: ')

        if not self._historico:
            print('Não existe transação registrada.')
        
        for data, transacao in self._historico:
            print(f'- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transacao}')  
        print('-------------------------------------\n')
