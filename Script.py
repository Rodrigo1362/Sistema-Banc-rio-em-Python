# Sistema Bancário Simples - Python
# Autor: Rodrigo Oliveira

menu = """
================ MENU ================

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Variáveis principais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    # DEPÓSITO
    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("✅ Depósito realizado com sucesso!")
            else:
                print("❌ Valor inválido para depósito.")
        except ValueError:
            print("❌ Entrada inválida. Digite um valor numérico.")

    # SAQUE
    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: R$ "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("❌ Saldo insuficiente.")
            elif excedeu_limite:
                print(f"❌ O limite por saque é de R$ {limite:.2f}.")
            elif excedeu_saques:
                print("❌ Número máximo de saques diários excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque:    R$ {valor:.2f}\n"
                numero_saques += 1
                print("✅ Saque realizado com sucesso!")
            else:
                print("❌ Valor inválido para saque.")
        except ValueError:
            print("❌ Entrada inválida. Digite um valor numérico.")

    # EXTRATO
    elif opcao == "e":
        print("\n=========== EXTRATO BANCÁRIO ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=========================================")

    # SAIR
    elif opcao == "q":
        print("\n👋 Obrigado por utilizar o sistema bancário. Até mais!")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("❌ Opção inválida. Tente novamente.")
