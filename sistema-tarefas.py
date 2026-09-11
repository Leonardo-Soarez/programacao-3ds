qtd_tarefas = int(input("Quantas tarefas deseja cadastrar? "))

lista_tarefas = []

for i in range(qtd_tarefas):
    nome = input(f"Digite a tarefa {i + 1}: ")
    lista_tarefas.append(nome)

banco_dados_tarefas = []

for id_tarefa, nome_tarefa in enumerate(lista_tarefas, start=1):
    prazo_dias = id_tarefa * 2
    status = "Pendente"

    tarefa = (id_tarefa, nome_tarefa, prazo_dias, status)
    banco_dados_tarefas.append(tarefa)

print("\n--- RESUMO DO SISTEMA ---")

for id_tarefa, nome_tarefa, prazo_dias, status in banco_dados_tarefas:
    print(
        f"ID: {id_tarefa} | "
        f"Tarefa: {nome_tarefa} | "
        f"Prazo: {prazo_dias} dias | "
        f"Status: {status}"
    )

print(f"\nTotal de tarefas processadas: {len(banco_dados_tarefas)}")
