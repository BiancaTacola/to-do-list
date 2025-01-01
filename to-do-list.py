# Simulador de Lista de Tarefas

def exibir_menu():
    print("\n===== Lista de Tarefas =====")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")


def adicionar_tarefa(lista):
    tarefa = input("Digite a nova tarefa: ")
    lista.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")


def listar_tarefas(lista):
    if not lista:
        print("A lista de tarefas está vazia!")
    else:
        print("\nTarefas:")
        for i, tarefa in enumerate(lista, start=1):
            print(f"{i}. {tarefa}")


def remover_tarefa(lista):
    listar_tarefas(lista)
    if lista:
        try:
            indice = int(
                input("Digite o número da tarefa que deseja remover: "))
            tarefa_removida = lista.pop(indice - 1)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        except (IndexError, ValueError):
            print("Número inválido! Tente novamente.")


def main():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
        elif opcao == "4":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
