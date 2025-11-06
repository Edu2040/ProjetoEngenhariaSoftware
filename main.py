from menu import fazer_cadastro, fazer_reserva

# Menu interativo
while True:
    print("1 - Cadastro")
    print("2 - Mostrar Cadastro")
    print("3 - Reserva")
    print("4 - Monstrar Reservas")

    x = int(input("\nEscolha um opção: "))

    if x == 1:
        fazer_cadastro()

    elif x == 2:
        with open("dados.json", "r") as arquivo:
            print(arquivo.read())

    elif x == 3:
        fazer_reserva()
