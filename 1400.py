import os
os.system("cls")


qtd = 0


while True:
    num = float(input("Número: "))
    dobro = num * 2
    print(f"P dobro de {num} é {dobro}")

    qtd = qtd + 1

    opcao = input("continuar, [s]im ou [n]ão?")
    
    while opcao != 's' and opcao != 'S' and opcao != 'n' and opcao != 'N':
        opcao = input("erro! s ou n?")
    else:
        if opcao == 'n' or opcao == 'N':
            break



print(f"Você calculou {qtd} vezes")
