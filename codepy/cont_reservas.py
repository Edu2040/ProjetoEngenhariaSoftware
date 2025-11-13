import os.path
import json

def contar_reservas():

    json_path = "codepy/filedata/dados.json"
    txt_path = "codepy/filedata/reserva.txt"

    # Verifica se o arquivo JSON e arquivo txt existem
    if not os.path.exists(json_path):
        print(f"Arquivo JSON ão encontrado: {json_path}")
        return
    if not os.path.exists(txt_path):
        print(f"Arquivo.txt de reservas não encontrado: {txt_path}")
        return

    # Abre o arquivo JSON e ler os dados dentro dele
    with open(json_path, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    # Verifica se "dados" é uma lista
    if isinstance(dados, list):
        nomes = [str(item.get("nome", "")).lower() for item in dados]
    # Verifica se é um dicionário
    elif isinstance(dados, dict):
        nomes = [str(dados.get("nome", "")).lower()]
    # Se não for nenhum desses ele aprensenta essa mensagem ↓
    else:
        print("Formato inesperado no JSON (esperado lista ou dicionário).")
        return

    # Leitura de linha por linha e verifica se não tem nenhum espaço em branco entre as reservas
    with open(txt_path, "r", encoding="latin-1") as arquivo:
        linhas = [linha.strip() for linha in arquivo.readlines() if linha.strip()]

    # Faz a leitura de cada texto
    pf_reservas = ["\n".join(linhas[i:i+2]) for i in range(0, len(linhas), 2)]

    nomes_unicos = sorted(set(nomes))

    # Recolhe os nomes e mostra a quantidade de reservas feitas por cada aluno
    for nome in nomes_unicos:
        if not nome:
            continue
        qtd = sum(1 for p in pf_reservas if nome in p.lower())
        print(f"{nome}: {qtd}")