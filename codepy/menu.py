from codepy.aluno import Aluno
from codepy.reserva import Reserva
from datetime import datetime

# Apenas para deixar o main.py mais organizado

def fazer_cadastro():
    try:
        nome = input("\nDigite o nome completo do aluno: \n")
        nome_title = nome.title()
        idade = int(input("Digite a idade: \n"))
        cpf = input("Digite o CPF do aluno: \n")
        plano = input("Planos: Mensal, 3 meses, 6 meses, 1 ano. \n\n")
        plano_cap = plano.capitalize()

        a = Aluno(nome_title, idade, cpf, plano_cap)
        a.cadastrar()
    except ValueError as e:
        print(f'Erro no cadastro: {e}')

def fazer_reserva():

    cpf = input("\nDigite o CPF do aluno: \n")
    atividade = input("Digite a atividade que deseja reservar (musculação, spinning, natação): \n")
    atividade_cap = atividade.capitalize()
    dataStr = input("Digite a data e hora para o dia da atividade (dia/mês/ano hora:minuto):\n")
    dataMarcada = datetime.strptime(dataStr, "%d/%m/%Y %H:%M").strftime("%d/%m/%Y %H:%M")
    status = input("Digite o status dessa atividade (Reservado, Confirmado, Concluído, Cancelado): \n")
    status_caps = status.capitalize()

    r = Reserva(cpf, atividade_cap, dataMarcada, status_caps)
    r.reservar()

def read_reservas():
    try:
        with open("codepy/filedata/reserva.txt", "r") as arquivo:
            print(arquivo.read())
    except Exception as e:
        print(f"Erro na leitura de arquivo: {e}")