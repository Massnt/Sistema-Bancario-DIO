class Conta:
    def __init__(self):
        self.__saldo = 0
        self.__historico = {'Saque':[], 'Deposito':[]}

    
    def __validar_valor(self,valor):
        if valor > 0:
            return True
        else:
            print('Valor inválido')
            return False


    def depositar(self, valor):
        if self.__validar_valor(valor):
            self.__saldo += valor
            self.__historico['Deposito'].append(valor)


    def sacar(self, valor):
        if valor > self.__saldo and self.__validar_valor(valor):
            print('Saldo insuficiente')
        else:
            self.__saldo -= valor
            self.__historico['Saque'].append(valor)

    
    def __str__(self):
        saque_str = '\n'.join([str(h) for h in self.__historico['Saque']])
        deposito_str = '\n'.join([str(h) for h in self.__historico['Deposito']])
        return f'''Saque
{saque_str}

Depósito
{deposito_str}'''
