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

        codMatricula = 'MAT' + ''.join(random.choices(string.digits, k=6))

        dadosregistro = {"nome": f"{self.nome}", "idade": f"{self.idade}", "cpf": f"{self.cpf}", "plano": f"{self.plano}", "matricula": codMatricula}

        if not os.path.exists("dados.json"):
            with open("dados.json", "w", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)

        with open("dados.json", "r", encoding="utf-8") as f:
            dados = json.load(f)

        dados.append(dadosregistro)

        with open("dados.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)