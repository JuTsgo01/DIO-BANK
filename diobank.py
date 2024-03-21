from datetime import date
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 1000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d": 
        valor_deposito =  float(input("Informe o Valor que deseja depositar: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Valor de depósito realizado foi de R$ {valor_deposito:.2f} no dia {date.today()}"
        else:
            print("Por favor, informe um valor acima de R$ 0.00 que seja válido")

    elif opcao == "s":
        valor_saque = float(input("Por favor, informe o valor que deseja depositar. Lembrando que o limite é 3 saque por dia de até R$ 500.00"))

        if valor_saque <= saldo and valor_saque <= limite and numero_saques <= LIMITE_SAQUES:
            saldo -= valor_saque
            extrato += f"\nO saque realizado foi de R$ {valor_saque:.2f} no dia {date.today()} "
            numero_saques += 1 

        else:
            if valor_saque > limite:
                print("Não será possível realizar o saque. Informamos o limite para saque é de R$ 500.00. Agradecemos por ser nosso cliente.")
            elif numero_saques > LIMITE_SAQUES:
                print("Não será possível realizar o saque. Informamos que a quantidade limite de saque é de 3 saques por dia. Agradecemos por ser nosso cliente.")
            elif valor_saque > saldo:
                print("Não será possível realizar o saque. Informamos que o seu saldo é menor que o valor de saque. Agradecemos por ser nosso cliente.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Agradecemos por ser nosso cliente. Até breve.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
