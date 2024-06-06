class Cores:
    VERMELHO = '\033[31m'
    VERDE = '\033[32m'
    AMARELO = '\033[33m'
    AZUL = '\033[34m'
    MAGENTA = '\033[35m'
    CIANO = '\033[36m'
    RESET = '\033[0m'

print(f"{Cores.MAGENTA}Seja Bem Vindo ao Banco COPIAeREFORMA{Cores.RESET}")
print(f'{Cores.AMARELO}${Cores.RESET}'*40)

menu = f"""
{Cores.VERMELHO}[d]{Cores.RESET} Depositar
{Cores.CIANO}[s]{Cores.RESET} Sacar
{Cores.VERDE}[e]{Cores.RESET} Extrato
{Cores.AZUL}[q]{Cores.RESET} Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print(f"{Cores.VERDE}\n=============== EXTRATO =================={Cores.RESET}")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"{Cores.VERDE}={Cores.RESET}"*45)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
print(f'{Cores.AMARELO}${Cores.RESET}'*40)