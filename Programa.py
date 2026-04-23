# Programa para analisar propriedades de uma relação em Matemática Discreta

# Função para verificar se a relação é reflexiva
def is_reflexiva(conjunto, relacao):
    for elemento in conjunto:
        # Verifica se (a, a) está na relação
        if (elemento, elemento) not in relacao:
            return False
    return True

# Função para verificar se a relação é simétrica
def is_simetrica(relacao):
    for (a, b) in relacao:
        # Verifica se (b, a) também está na relação
        if (b, a) not in relacao:
            return False
    return True

# Função para verificar se a relação é transitiva
def is_transitiva(relacao):
    for (a, b) in relacao:
        for (c, d) in relacao:
            # Se (a, b) e (b, c) existem, então (a, c) deve existir
            if b == c and (a, d) not in relacao:
                return False
    return True

# Entrada do conjunto
print("Digite os elementos do conjunto separados por espaço:")
conjunto = input().split()

# Entrada da relação
print("Digite os pares da relação no formato a,b (um por linha). Digite 'fim' para encerrar:")
relacao = []

while True:
    entrada = input()
    if entrada.lower() == "fim":
        break
    a, b = entrada.split(",")
    relacao.append((a.strip(), b.strip()))

# Converte para conjunto para facilitar buscas
relacao = set(relacao)

# Verifica as propriedades
print("\nResultados:")

if is_reflexiva(conjunto, relacao):
    print("A relação é reflexiva")
else:
    print("A relação NÃO é reflexiva")

if is_simetrica(relacao):
    print("A relação é simétrica")
else:
    print("A relação NÃO é simétrica")

if is_transitiva(relacao):
    print("A relação é transitiva")
else:
    print("A relação NÃO é transitiva")