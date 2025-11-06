from menu import fazer_cadastro, fazer_reserva, read_reservas

# Menu interativo
while True:
    print("1 - Cadastro")
    print("2 - Mostrar Cadastros")
    print("3 - Reserva")

    x = int(input("\nEscolha um opção: "))

    if x == 1:
        fazer_cadastro()

    elif x == 2:
        fazer_reserva()

    elif x == 3:
        read_reservas()