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

        # Formato JSON que é enviado para os dados.json, é preenchido com todos os parâmetros
        dadosregistro = {"nome": f"{self.nome}", "idade": f"{self.idade}", "cpf": f"{self.cpf}", "plano": f"{self.plano}"}

        # Verifica se o arquivo existe e se não existir é criado um arquivo com o nome dados.json
        if not os.path.exists("codepy/filedata/dados.json"):
            with open("codepy/filedata/dados.json", "w", encoding="utf-8") as f:
                # Faz com que o arquivo JSON não perca o formato dele
                json.dump([], f, indent=4, ensure_ascii=False)

        # Apenas lê o arquivo JSON
        with open("codepy/filedata/dados.json", "r", encoding="utf-8") as f:
            dados = json.load(f)

        # Evita duplicação de CPF
        for aluno in dados:
            if aluno["cpf"] == self.cpf:
                raise ValueError("Já existe um aluno cadastrado com esse CPF.")

        # Após todos os parâmetros preenchidos e a verificação feita é adicionado no JSON o dados de registro
        dados.append(dadosregistro)

        # Escreve o conteúdo da variável dados, formata o arquivo JSON com uma identação bonita e permite ter suporte a caracteres especiais
        with open("codepy/filedata/dados.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)