def calculadora():
    print("--- Calculadora Simples em Python ---")
    print("Operações disponíveis:")
    print("1: Soma (+)")
    print("2: Subtração (-)")
    print("3: Multiplicação (*)")
    print("4: Divisão (/)")

    # Recebendo a escolha do usuário
    escolha = input("\nDigite o número da operação (1/2/3/4): ")

    # Solicitando os números para o cálculo
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Lógica das operações
    if escolha == '1':
        resultado = num1 + num2
        print(f"\nResultado: {num1} + {num2} = {resultado}")
    elif escolha == '2':
        resultado = num1 - num2
        print(f"\nResultado: {num1} - {num2} = {resultado}")
    elif escolha == '3':
        resultado = num1 * num2
        print(f"\nResultado: {num1} * {num2} = {resultado}")
    elif escolha == '4':
        # Verificação para evitar divisão por zero
        if num2 != 0:
            resultado = num1 / num2
            print(f"\nResultado: {num1} / {num2} = {resultado}")
        else:
            print("\nErro: Não é possível dividir por zero!")
    else:
        print("\nOpção inválida. Tente novamente.")

# Executa a função
calculadora()
