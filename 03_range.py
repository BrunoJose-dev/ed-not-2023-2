# range() é uma função que gera uma faixa de números.
#É muito usada em associação com listas.

# 1) range() com 1 parâmetro: gera uma faixa que vai de 
# 0 (zero) até o valor do parãmetro -1
for num in range(10):
    print(num)

print("-" * 40)  # Traço de 40 hífens

# 2) range() com 2 parâmetros: gera uma sequência começando
# pelo valor do primeiro parâmetro (inclusive) e indo até 
# o valor do segundo parâmetro (exclusive, NÃO ENTRA)
for i in range(10,15):
    print(i)

print("-" * 40)  # Traço de 40 hífens

# 3)  range() com 3 parâmetros
#     1°: limite inferior (inclusive)
#     2°: limite superior (exclusive, NÃO ENTRA)
#     3°: passo (de quanto em quanto a sequência vai saltar; PODE SER NEGATIVO)
for i in range(1, 22, 3):   # De 1 a 22 salatando de 3 em 3
    print(i)

print("-" * 40)  # Traço de 40 hífens

# range() com passo negativo
for i in range(10, 0, -1):   # Contagem regressiva de 10 a 1
    print(i)

