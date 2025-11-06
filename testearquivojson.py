from InquirerPy import inquirer

while True:
    opcao = inquirer.select(
        message="Selecione uma opção:",
        choices=[
            "Cadastrar aluno",
            "Buscar aluno",
            "Gerar relatório PDF",
            "Sair"
        ],
    ).execute()

    if opcao == "Cadastrar aluno":
        print("➡ Cadastrando aluno...")
    elif opcao == "Buscar aluno":
        print("🔍 Buscando aluno...")
    elif opcao == "Gerar relatório PDF":
        print("🧾 Gerando relatório...")
    elif opcao == "Sair":
        print("👋 Encerrando programa.")
        break
