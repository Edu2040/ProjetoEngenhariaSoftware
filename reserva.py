from datetime import datetime
import json

class Reserva:
    def __init__(self, matricula, atividade, datahora, status):
        self.matricula = matricula
        self.atividade = atividade
        self.datahora = datahora
        self.status = status


    def reservar(self):

        datareserva = datetime.now()
        reformadatarv = datareserva.strftime("%d/%m/%Y %H:%M:%S")

        with open("dados.json", "r", encoding="utf-8") as arquivo:
            lerDados = json.load(arquivo)

        for lerDados in lerDados:
            if lerDados["matricula"] == self.matricula:
                name = lerDados["nome"]

        with open("reserva.txt", "a") as arquivo:
            arquivo.write(f"Horário que a reserva foi feita {reformadatarv}\nAluno(a) {name} fez uma reserva para o dia {self.datahora}"
                        f" na atividade {self.atividade}\nStatus da reserva: {self.status}\n\n")