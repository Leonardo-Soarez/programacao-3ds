# 1. Lista de nomes de estudantes
estudantes = ["Carlos", "Ana", "Pedro", "Beatriz", "Mariana"]

# Use sort() para ordenar diretamente a lista original em ordem decrescente
estudantes.sort(reverse=True)
print("Estudantes ordenados (decrescente):", estudantes)


# Exemplo de uma lista original
lista_original = [5, 2, 9, 1, 7]

# 1. Ordem Crescente (padrão)
lista_crescente = sorted(lista_original)

# 2. Ordem Decrescente (ajustando o reverse para True)
lista_decrescente = sorted(lista_original, reverse=True)

# Impressão das listas conforme pedido no enunciado
print("Lista original:", lista_original)
print("Ordem crescente:", lista_crescente)
print("Ordem decrescente:", lista_decrescente)
