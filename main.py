from codepy.menu import fazer_cadastro, fazer_reserva, read_reservas
from codepy.cont_reservas import contar_reservas

# Menu interativo

while True:
    print("\n====|MENU ACADEMIA|====")
    print("1 - Cadastro")
    print("2 - Reservar")
    print("3 - Mostrar reservas")
    print("4 - Quantidade de reservas por aluno")

    op = int(input("\nEscolha um opção: "))

    if op == 1:
        fazer_cadastro()

    elif op == 2:
        fazer_reserva()

    elif op == 3:
        read_reservas()

    elif op == 4:
        contar_reservas()