from codepy.menu import fazer_cadastro, fazer_reserva, read_reservas
from codepy.cont_reservas import contar_reservas

# Menu interativo
while True:
    print("1 - Cadastro")
    print("2 - Reservar")
    print("3 - Mostrar reservas")
    print("4 - Quantidade de reservas por aluno")

    x = int(input("\nEscolha um opção: "))

    if x == 1:
        fazer_cadastro()

    elif x == 2:
        fazer_reserva()

    elif x == 3:
        read_reservas()

    elif x == 4:
        contar_reservas()