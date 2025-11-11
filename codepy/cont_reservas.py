import os.path
import json


def contar_reservas():

    json_path = "codepy/filedata/dados.json"
    txt_path = "codepy/filedata/reserva.txt"

    if not os.path.exists(json_path):
        print(f"Arquivo JSON ão encontrado: {json_path}")
        return
    if not os.path.exists(txt_path):
        print(f"Arquivo.txt de reservas não encontrado: {txt_path}")
        return

    with open(json_path, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    if isinstance(dados, list):
        nomes = [str(item.get("nome", "")).lower() for item in dados]
    elif isinstance(dados, dict):
        nomes = [str(dados.get("nome", "")).lower()]
    else:
        print("Formato inesperado no JSON (esperado lista ou dicionário).")
        return

    with open(txt_path, "r", encoding="latin-1") as arquivo:
        linhas = [linha.strip() for linha in arquivo.readlines() if linha.strip()]

    pf_reservas = ["\n".join(linhas[i:i+2]) for i in range(0, len(linhas), 2)]

    nomes_unicos = sorted(set(nomes))

    for nome in nomes_unicos:
        if not nome:
            continue
        qtd = sum(1 for p in pf_reservas if nome in p.lower())
        print(f"{nome}: {qtd}")