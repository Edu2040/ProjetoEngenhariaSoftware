import random
import string
import json
import os.path

class Aluno:
    def __init__(self, nome, idade, cpf, plano):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.plano = plano


    def cadastrar(self):

        #codMatricula = 'MAT' + ''.join(random.choices(string.digits, k=6))

        #num_reservas = "0"

        dadosregistro = {"nome": f"{self.nome}", "idade": f"{self.idade}", "cpf": f"{self.cpf}", "plano": f"{self.plano}"}

        if not os.path.exists("codepy/filedata/dados.json"):
            with open("codepy/filedata/dados.json", "w", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)

        with open("codepy/filedata/dados.json", "r", encoding="utf-8") as f:
            dados = json.load(f)

        dados.append(dadosregistro)

        with open("codepy/filedata/dados.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)