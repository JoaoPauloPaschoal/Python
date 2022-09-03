from time import sleep

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
menu = 0
while menu != 5:
    print(""" 
[1] - Adição (+)
[2] - Subtração (-)
[3] - Multiplicação (*)
[4] - Divisão (/)
[5] - Encerrar """)
    menu = int(input("\nDigite a opção desejada: "))

    if menu == 1:
        adicao = n1 + n2
        print("A soma de {} por {} é = {} ".format(n1, n2, adicao))
    elif menu == 2:
        subtracao = n1 - n2
        print("A subtração de {} por {} é = {} ".format(n1, n2, subtracao))
    elif menu == 3:
        multi = n1 * n2
        print("A multiplicação de {} por {} é = {} ".format(n1, n2, multi))
    elif menu == 4:
        divisao = n1 / n2
        print("A divisão de {} por {} é = {} ".format(n1, n2, divisao))
    else:
        print("\nFinalizando\n")
    sleep(1)
print("Fim do Programa")

