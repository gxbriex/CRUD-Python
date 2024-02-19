lista_alunos = []
lista_professores = []
lista_disciplinas = []
lista_turmas = []
lista_matriculas = []


def menu_principal():
    print("Saudações! Bem vindo ao menu principal.")
    print("(1) Estudantes")
    print("(2) Professores")
    print("(3) Disciplinas")
    print("(4) Turmas")
    print("(5) Matrículas")
    print("(6) Sair")
    return input("Escolha uma opção: ")


def menu_secundario():
    print("(1) Incluir")
    print("(2) Listar")
    print("(3) Atualizar")
    print("(4) Excluir")
    print("(5) Voltar ao menu principal")
    return input("Qual a opção que deseja executar?: ")


def incluir(lista, solicitar_cpf=True):
    print("Você escolheu a opção INCLUIR.")
    nome = input("Digite o nome que deseja incluir: ")
    cpf = ""
    item_id = ""
    if solicitar_cpf:
        cpf = input("Digite o CPF: ")
        while True:
            item_id_str = input("Digite um ID para cadastro: ")
            if item_id_str.isdigit():
                item_id = int(item_id_str)
                if not any(item["ID"] == item_id for item in lista):
                    break
                else:
                    print("O ID já existe. Por favor, escolha outro.")
            else:
                print("ID inválido. Digite um número inteiro válido.")
    dados = {
        "Nome": nome,
        "CPF": cpf,
        "ID": item_id
    }
    lista.append(dados)
    print("Cadastrado!")


def listar(lista):
    print("Você escolheu a opção LISTAR.")
    print("Dados armazenados: ")
    for item in lista:
        print(item)


def atualizar(lista):
    print("Você escolheu a opção ATUALIZAR")
    try:
        atualizar_id = int(
            input("Digite o ID que deseja atualizar: "))
        id_encontrado = False
        for item in lista:
            if item["ID"] == atualizar_id:
                print(f"ID: {item['ID']}, Nome: {item['Nome']}, CPF: {item['CPF']}")
                editar_nome = input("Atualize o nome: ")
                editar_cpf = input("Atualize o CPF ou mantenha o mesmo: ")
                if editar_nome:
                    item['Nome'] = editar_nome
                if editar_cpf:
                    item['CPF'] = editar_cpf
                print("Atualizado.")
                id_encontrado = True
                break
        if not id_encontrado:
            print("Não foi possível achar o ID.")
    except ValueError:
        print("O ID deve ser um número inteiro.")


def excluir(lista):
    print("Você escolheu a opção EXCLUIR.")
    try:
        excluir_id = int(input("Qual ID deseja excluir?: "))
        for item in lista:
            if item["ID"] == excluir_id:
                lista.remove(item)
                print("Removido.")
                break
        else:
            print("ID não encontrado.")
    except ValueError:
        print("O ID deve ser um número inteiro.")
    print(lista)


def incluir_disciplina(lista_disciplinas):
    print("Você escolheu a opção INCLUIR DISCIPLINA.")
    nome_disciplina = input("Digite o nome da disciplina: ")
    id_disciplina = ""
    while True:
        id_disciplina_str = input("Digite o ID da disciplina: ")
        if id_disciplina_str.isdigit():
            id_disciplina = int(id_disciplina_str)
            break
        else:
            print("ID inválido. Digite um número inteiro válido.")
    dados = {
        "Nome": nome_disciplina,
        "ID": id_disciplina
    }
    lista_disciplinas.append(dados)
    print("Disciplina cadastrada.")


def listar_disciplinas(lista_disciplinas):
    print("Você escolheu a opção LISTAR DISCIPLINAS.")
    print("Disciplinas cadastradas:")
    for disciplina in lista_disciplinas:
        print(f"Nome: {disciplina['Nome']}, ID: {disciplina['ID']}")


def atualizar_disciplina(lista_disciplinas):
    print("Você escolheu a opção ATUALIZAR DISCIPLINA.")
    try:
        atualizar_id = int(input("Digite o ID da disciplina que deseja atualizar: "))
    except ValueError:
        print("ID deve ser um número inteiro.")
        return
    for disciplina in lista_disciplinas:
        if disciplina["ID"] == atualizar_id:
            print(f"ID: {disciplina['ID']}, Nome: {disciplina['Nome']}")
            novo_nome = input("Atualize o nome da disciplina ou mantenha o mesmo: ")
            if novo_nome:
                disciplina['Nome'] = novo_nome
            print("Disciplina atualizada.")
            break
    else:
        print("ID não encontrado.")


def excluir_disciplina(lista_disciplinas):
    print("Você escolheu a opção EXCLUIR DISCIPLINA.")
    excluir_id = input("Digite o ID da disciplina que deseja excluir: ")
    for disciplina in lista_disciplinas:
        if disciplina["ID"] == excluir_id:
            lista_disciplinas.remove(disciplina)
            print("Disciplina removida.")
            break
    else:
        print("ID não encontrado.")


def incluir_turma(lista_turmas, lista_professores, lista_disciplinas):
    print("Você escolheu a opção INCLUIR TURMA.")
    id_turma = ""
    id_professor = ""
    id_disciplina = ""
    while True:
        id_turma_str = input("Digite o ID da turma: ")
        if id_turma_str.isdigit():
            id_turma = int(id_turma_str)
            break
        else:
            print("ID da turma inválido.")
    while True:
        id_professor_str = input("Digite o ID do professor: ")
        if id_professor_str.isdigit():
            id_professor = int(id_professor_str)
            break
        else:
            print("ID do professor inválido.")
    while True:
        id_disciplina_str = input("Digite o ID da disciplina: ")
        if id_disciplina_str.isdigit():
            id_disciplina = int(id_disciplina_str)
            break
        else:
            print("ID da disciplina inválido.")
    professor_existente = any(professor["ID"] == id_professor for professor in lista_professores)
    disciplina_existente = any(disciplina["ID"] == id_disciplina for disciplina in lista_disciplinas)
    if professor_existente and disciplina_existente:
        if any(turma["ID Turma"] == id_turma for turma in lista_turmas):
            print("A turma com este ID já existe. Por favor, escolha outro.")
            return
        turma = {
            "ID Turma": id_turma,
            "ID Professor": id_professor,
            "ID Disciplina": id_disciplina
        }
        lista_turmas.append(turma)
        print("Turma cadastrada.")
    else:
        print("Professor ou disciplina não encontrados.")


def listar_turmas(lista_turmas):
    print("Você escolheu a opção LISTAR TURMAS.")
    if not lista_turmas:
        print("Nenhuma turma cadastrada.")
    else:
        print("Turmas cadastradas:")
        for turma in lista_turmas:
            print(
                f"ID Turma: {turma['ID Turma']}, ID Professor: {turma['ID Professor']}, ID Disciplina: {turma['ID Disciplina']}")


def atualizar_turma(lista_turmas, lista_professores, lista_disciplinas):
    print("Você escolheu a opção ATUALIZAR TURMA.")
    try:
        id_turma = int(input("Digite o ID da turma que deseja atualizar: "))
        novo_id_professor = int(input("Digite o novo ID do professor ou mantenha o mesmo: "))
        novo_id_disciplina = int(input("Digite o novo ID da disciplina ou mantenha o mesmo: "))
    except ValueError:
        print("Os IDs devem ser números inteiros.")
        return
    for turma in lista_turmas:
        if turma["ID Turma"] == id_turma:
            professor_existente = any(professor["ID"] == novo_id_professor for professor in lista_professores)
            disciplina_existente = any(disciplina["ID"] == novo_id_disciplina for disciplina in lista_disciplinas)
            if professor_existente and disciplina_existente:
                turma["ID Professor"] = novo_id_professor
                turma["ID Disciplina"] = novo_id_disciplina
                print("Turma atualizada.")
            else:
                print("Professor ou disciplina não encontrados.")
            break
    else:
        print("ID da turma não encontrado.")


def excluir_turma(lista_turmas):
    print("Você escolheu a opção EXCLUIR TURMA.")
    id_turma = input("Digite o ID da turma que deseja excluir: ")
    for turma in lista_turmas:
        if turma["ID Turma"] == id_turma:
            lista_turmas.remove(turma)
            print("Turma removida.")
            break
    else:
        print("ID da turma não encontrado.")


def incluir_matricula(lista_matriculas, lista_turmas, lista_alunos):
    print("Você escolheu a opção INCLUIR MATRÍCULA.")
    id_turma = ""
    id_estudante = ""
    while True:
        id_turma_str = input("Digite o ID da turma: ")
        if id_turma_str.isdigit():
            id_turma = int(id_turma_str)
            break
        else:
            print("ID da turma inválido. Digite um número inteiro válido.")
    while True:
        id_estudante_str = input("Digite o ID do estudante: ")
        if id_estudante_str.isdigit():
            id_estudante = int(id_estudante_str)
            break
        else:
            print("ID do estudante inválido.")
    id_matricula = len(lista_matriculas) + 1
    matricula = {
        "ID Matrícula": id_matricula,
        "ID Turma": id_turma,
        "ID Estudante": id_estudante
    }
    lista_matriculas.append(matricula)
    print("Matrícula cadastrada.")


def listar_matriculas(lista_matriculas, lista_turmas, lista_alunos):
    print("Você escolheu a opção LISTAR MATRÍCULAS.")
    if not lista_matriculas:
        print("Nenhuma matrícula realizada.")
    else:
        print("Matrículas realizadas:")
        for matricula in lista_matriculas:
            turma = next((turma for turma in lista_turmas if turma["ID Turma"] == matricula["ID Turma"]), None)
            aluno = next((aluno for aluno in lista_alunos if aluno["ID"] == matricula["ID Estudante"]), None)
            if turma and aluno:
                print(f"ID Turma: {matricula['ID Turma']}, ID Estudante: {matricula['ID Estudante']}")
                print(f"Nome da Turma: {turma['ID Turma']}, Nome do Estudante: {aluno['Nome']}")
                print()
            else:
                print("Turma ou aluno não encontrados.")


def atualizar_matricula(lista_matriculas, lista_turmas, lista_alunos):
    print("Você escolheu a opção ATUALIZAR MATRÍCULA.")
    id_matricula = int(input("Digite o ID da matrícula que deseja atualizar: "))
    matricula = next((matricula for matricula in lista_matriculas if matricula["ID Matrícula"] == id_matricula), None)
    if matricula:
        novo_id_estudante = int(input("Digite o novo ID do estudante ou mantenha o mesmo: "))
        aluno_existente = any(aluno["ID"] == novo_id_estudante for aluno in lista_alunos)
        if aluno_existente:
            id_turma = matricula["ID Turma"]
            turma_existente = any(turma["ID Turma"] == id_turma for turma in lista_turmas)
            if turma_existente:
                matricula["ID Estudante"] = novo_id_estudante
                print("Matrícula atualizada com sucesso.")
            else:
                print("ID da turma não encontrado.")
        else:
            print("ID do estudante não encontrado.")
    else:
        print("Matrícula não encontrada.")


def excluir_matricula(lista_matriculas):
    print("Você escolheu a opção EXCLUIR MATRÍCULA.")
    id_turma = input("Digite o ID da turma da matrícula que deseja excluir: ")
    id_estudante = input("Digite o ID do estudante da matrícula que deseja excluir: ")
    matricula = next((matricula for matricula in lista_matriculas if
                      matricula["ID Turma"] == id_turma and matricula["ID Estudante"] == id_estudante), None)
    if matricula:
        lista_matriculas.remove(matricula)
        print("Matrícula removida.")
    else:
        print("Matrícula não encontrada.")


while True:
    menu = menu_principal()
    if menu == "1":
        print("Você escolheu a opção ESTUDANTES")
        while True:
            alternativa = menu_secundario()
            if alternativa == "1":
                incluir(lista_alunos)
            elif alternativa == "2":
                listar(lista_alunos)
            elif alternativa == "3":
                atualizar(lista_alunos)
            elif alternativa == "4":
                excluir(lista_alunos)
            elif alternativa == "5":
                print("Voltando ao Menu Principal...")
                break
            else:
                print("Você digitou algo errado...")
    elif menu == "2":
        print("Você escolheu a opção PROFESSORES.")
        while True:
            alternativa = menu_secundario()
            if alternativa == "1":
                incluir(lista_professores)
            elif alternativa == "2":
                listar(lista_professores)
            elif alternativa == "3":
                atualizar(lista_professores)
            elif alternativa == "4":
                excluir(lista_professores)
            elif alternativa == "5":
                print("Voltando ao Menu Principal...")
                break
            else:
                print("Você digitou algo errado...")
    elif menu == "3":
        print("Você escolheu a opção DISCIPLINAS.")
        while True:
            alternativa = menu_secundario()
            if alternativa == "1":
                incluir_disciplina(lista_disciplinas)
            elif alternativa == "2":
                listar_disciplinas(lista_disciplinas)
            elif alternativa == "3":
                atualizar_disciplina(lista_disciplinas)
            elif alternativa == "4":
                excluir_disciplina(lista_disciplinas)
            elif alternativa == "5":
                print("Voltando ao menu principal...")
                break
            else:
                print("Você digitou algo errado.")
    elif menu == "4":
        print("Você escolheu a opção TURMAS.")
        while True:
            alternativa = menu_secundario()
            if alternativa == "1":
                incluir_turma(lista_turmas, lista_professores, lista_disciplinas)
            elif alternativa == "2":
                listar_turmas(lista_turmas)
            elif alternativa == "3":
                atualizar_turma(lista_turmas, lista_professores, lista_disciplinas)
                pass
            elif alternativa == "4":
                excluir_turma(lista_turmas)
                pass
            elif alternativa == "5":
                print("Voltando ao menu principal...")
                break
            else:
                print("Você digitou algo errado.")
    elif menu == "5":
        print("Você escolheu a opção MATRÍCULAS.")
        while True:
            alternativa_matriculas = menu_secundario()
            if alternativa_matriculas == "1":
                incluir_matricula(lista_matriculas, lista_turmas, lista_alunos)
            elif alternativa_matriculas == "2":
                listar_matriculas(lista_matriculas, lista_turmas, lista_alunos)
            elif alternativa_matriculas == "3":
                atualizar_matricula(lista_matriculas, lista_turmas, lista_alunos)
            elif alternativa_matriculas == "4":
                excluir_matricula(lista_matriculas)
            elif alternativa_matriculas == "5":
                print("Voltando ao menu principal...")
                break
            else:
                print("Você digitou algo errado...")
    elif menu == "6":
        print("Finalizando aplicação...")
        break
    else:
        print("Você digitou algo errado!")