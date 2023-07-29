class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para saque ou valor inválido.")

    def verificar_saldo(self):
        print(f"Saldo disponível: R${self.saldo:.2f}")


def main():
    contas = {}

    while True:
        print("\n===== Bem-vindo ao Sistema Bancário =====")
        print("1. Criar conta")
        print("2. Acessar conta")
        print("3. Sair")
        escolha = input("Digite a opção desejada (1/2/3): ")

        if escolha == '1':
            nome_titular = input("Digite o nome do titular da conta: ")
            saldo_inicial = float(input("Digite o saldo inicial: "))
            conta = ContaBancaria(nome_titular, saldo_inicial)
            contas[nome_titular] = conta
            print(f"Conta criada para {nome_titular} com saldo inicial de R${saldo_inicial:.2f}.")

        elif escolha == '2':
            nome_titular = input("Digite o nome do titular da conta: ")
            if nome_titular in contas:
                conta = contas[nome_titular]
                while True:
                    print(f"\n===== Bem-vindo(a), {nome_titular} =====")
                    print("1. Depositar")
                    print("2. Sacar")
                    print("3. Verificar saldo")
                    print("4. Voltar ao menu principal")
                    escolha_conta = input("Digite a opção desejada (1/2/3/4): ")

                    if escolha_conta == '1':
                        valor_deposito = float(input("Digite o valor a ser depositado: "))
                        conta.depositar(valor_deposito)

                    elif escolha_conta == '2':
                        valor_saque = float(input("Digite o valor a ser sacado: "))
                        conta.sacar(valor_saque)

                    elif escolha_conta == '3':
                        conta.verificar_saldo()

                    elif escolha_conta == '4':
                        break
                    else:
                        print("Opção inválida. Tente novamente.")

            else:
                print("Conta não encontrada. Verifique o nome do titular.")

        elif escolha == '3':
            print("Obrigado por utilizar o Sistema Bancário. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
