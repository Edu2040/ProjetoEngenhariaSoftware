import json
import os.path

class Aluno:
    def __init__(self, nome, idade, cpf, plano):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.plano = plano

    def validar(self):
        # Nome não pode ser vazio
        if not self.nome:
            raise ValueError("O nome do aluno não pode estar vazio.")
        # Idade precisa ser número positivo
        if not isinstance(self.idade, int) or self.idade <= 0:
            raise ValueError("Idade inválida.")
        # CPF deve ter apenas números e ter 11 dígitos
        if not (self.cpf.isdigit() and len(self.cpf) == 11):
            raise ValueError("CPF inválido. Deve conter 11 números.")
        # Plano deve estar entre os disponíveis
        planos_validos = ["Mensal", "3 meses", "6 meses", "1 ano"]
        if self.plano not in planos_validos:
            raise ValueError(f"Plano inválido. Opções válidas: {', '.join(planos_validos)}")

    def cadastrar(self):
        self.validar()

        dadosregistro = {"nome": f"{self.nome}", "idade": f"{self.idade}", "cpf": f"{self.cpf}", "plano": f"{self.plano}"}

        if not os.path.exists("codepy/filedata/dados.json"):
            with open("codepy/filedata/dados.json", "w", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)

        with open("codepy/filedata/dados.json", "r", encoding="utf-8") as f:
            dados = json.load(f)

        # Evita duplicação de CPF
        for aluno in dados:
            if aluno["cpf"] == self.cpf:
                raise ValueError("Já existe um aluno cadastrado com esse CPF.")

        dados.append(dadosregistro)

        with open("codepy/filedata/dados.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)