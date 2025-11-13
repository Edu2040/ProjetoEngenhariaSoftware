from datetime import datetime
import json
import os.path

class Reserva:
    def __init__(self, cpf, atividade, datahora, status):
        self.cpf = cpf
        self.atividade = atividade
        self.datahora = datahora
        self.status = status

    # Valida cada entrada de parâmetro atrás de erros
    def validar(self):
        if not os.path.exists("codepy/filedata/dados.json"):
            raise FileNotFoundError("Nenhum aluno cadastrado ainda.")
        with open("codepy/filedata/dados.json", "r", encoding="utf-8") as arquivo:
            alunos = json.load(arquivo)

        aluno_encontrado = next((a for a in alunos if a["cpf"] == self.cpf), None)
        if not aluno_encontrado:
            raise ValueError("CPF não encontrada.")

        atividades_validas = ["Musculação", "Spinning", "Natação"]
        if self.atividade not in atividades_validas:
            raise ValueError(f"Atividade inválida. Opções: {', '.join(atividades_validas)}")

        status_validos = ["Reservado", "Confirmado", "Concluído", "Cancelado"]
        if self.status not in status_validos:
            raise ValueError(f"Status inválido. Opções: {', '.join(status_validos)}")

        return aluno_encontrado

    # Faz a reserva
    def reservar(self):

        # Avalia os parâmetros que vão ser usados para fazer a reserva
        self.validar()

        # Pega a data atual e reformula a data para o padrão conhecido
        datareserva = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Leitura dos dados JSON
        with open("codepy/filedata/dados.json", "r", encoding="utf-8") as arquivo:
            lerDados = json.load(arquivo)

        # Procura o CPF no arquivo JSON e pega o nome do dono do CPF
        for lerDados in lerDados:
            if lerDados["cpf"] == self.cpf:
                name = lerDados["nome"]

        # O nome é colocado no texto de reserva e é escrito no arquivo.txt
        with open("codepy/filedata/reserva.txt", "a") as arquivo:
            arquivo.write(f"Reserva feita {datareserva}\n{name} fez uma reserva para o dia {self.datahora}"
                        f" na atividade {self.atividade} | Status da reserva: {self.status}\n\n")

