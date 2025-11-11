from datetime import datetime
import json

class Reserva:
    def __init__(self, cpf, atividade, datahora, status):
        self.cpf = cpf
        self.atividade = atividade
        self.datahora = datahora
        self.status = status


    def reservar(self):

        datareserva = datetime.now()
        reformadatarv = datareserva.strftime("%d/%m/%Y %H:%M:%S")

        with open("codepy/filedata/dados.json", "r", encoding="utf-8") as arquivo:
            lerDados = json.load(arquivo)

        for lerDados in lerDados:
            if lerDados["cpf"] == self.cpf:
                name = lerDados["nome"]

        with open("codepy/filedata/reserva.txt", "a") as arquivo:
            arquivo.write(f"Reserva feita {reformadatarv}\n{name} fez uma reserva para o dia {self.datahora}"
                        f" na atividade {self.atividade} | Status da reserva: {self.status}\n\n")

