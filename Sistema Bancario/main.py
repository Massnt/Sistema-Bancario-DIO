from conta import Conta

cliente_conta = Conta()

print('''Menu
1| Depositar
2| Sacar
3| Historico
4| Sair
''')
while True:
    opr = input('Digite qual operação deseja realizar:')
    # Para não fazer um tratamento para entrada, simplismente usaremos como str e o match
    # case já faz o tratamento necessário

    match opr:
        case '1':
            valor = float(input('Digite o valor do depósito:'))
            cliente_conta.depositar(valor)

        case '2':
            valor = float(input('Digite o valor do Saque:'))
            cliente_conta.sacar(valor)

        case '3':
            print(cliente_conta)

        case '4':
            print('Volte sempre')
            break

        case _:
            print('Operação inválida')
            continue

