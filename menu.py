from aluno import Aluno
from reserva import Reserva
from datetime import datetime


def fazer_cadastro():
    nome = input("\nDigite o nome completo do aluno: \n")
    idade = int(input("Digite a idade: \n"))
    cpf = input("Digite o CPF do aluno: \n")
    plano = input("Planos: Mensal, 3 meses, 6 meses, 1 ano. \n")

    a = Aluno(nome, idade, cpf, plano)
    a.cadastrar()

def fazer_reserva():
    matricula = input("\nDigite a matrícula do aluno: \n")
    atividade = input("Digite a atividade que deseja reservar (musculação, spinning, natação): \n")
    dataStr = input("Digite a data e hora para o dia da atividade (dia/mês/ano hora:minuto):\n")
    dataMarcada = datetime.strptime(dataStr, "%d/%m/%Y %H:%M")
    status = input("Digite o status dessa atividade (Reservado, Confirmado, Concluído, Cancelado): \n")
    print

    r = Reserva(matricula, atividade, dataMarcada, status)
    r.reservar()