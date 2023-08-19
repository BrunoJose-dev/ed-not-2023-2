# LISTAS
# Listas são uma forma de armazenar mais de um valor em uma
# única variável. Os valores podem ser de tipos diferentes.

# Uma lista de números
valores = [2, 3, 5, 7, 9, 11]

# Uma lista com valores de tipos variados
mix = ["batata", 1.25, True, "tomate", 44]

# Lista de strings
legumes = ["batata", "tomate", "abobrinha", "cenoura"]

# OPERAÇÕES SOBRE LISTAS

# 1) PERCURSO: significa percorrer a lista do primeiro ao
#    último elemento, fazendo algo com cada um deles.

# Imprimindo cada um dos elementos da lista, um por linha:
for val in valores:
    print(val)

print("-" * 40)  # Traço de 40 hífens

# Imprimindo o dobro do valor de cada elemento da lista
for x in valores:
    print(x * 2)

print("-" * 40)  # Traço de 40 hífens

# 2) INSERINDO UM NOVO ELEMENTO NO *FIM* DA LISTA

valores.append(13)
legumes.append("cebola")

print(valores)
print(legumes)

print("-" * 40)  # Traço de 40 hífens

# 3) INSERINDO UM NOVO ELEMENTO EM UMA POSIÇÃO ESPECIFICADA
#    Parâmetros:
#    1º: a posição onde será inserido o novo elemento
#    2º: o novo elemento a ser inserido

legumes.insert(2, "mandioquinha")
print(legumes)
legumes.insert(0, "beterraba")
print(legumes)

print("-" * 40)  # Traço de 40 hífens

# 4) ACESSANDO UM VALOR EM UMA POSIÇÃO ESPECÍFICA
print("Elemento na QUARTA posição:", valores[3])
print("Elemento na PRIMEIRA posição: ", valores[0])
print("Elemento na ÚLTIMA posição: ", valores[-1])
print("Elemento na PENÚLTIMA posição: ", valores[-2])

print("-" * 40)  # Traço de 40 hífens
# 5) substituindo valores existentes
legumes[3] = "vagem"
#substituindo o valor da posição 0
legumes[0] = "mandioca"
#substituindo o valor da última posição
legumes[-1] = "milho"

print("-" * 40)  # Traço de 40 hífens

# 6) determinando a quantidade de elementos na lista: len()
print("número de elementos na lista de valores: ", len(valores))
print("número de elementos na lista de legumes: ", len(legumes))

print("-" * 40)  # Traço de 40 hífens

#7) Removendo o último elemento de uma lista: pop()
print("ANTES: ", valores)
removido = valores.pop()
print("Valor removido: ", removido)
print("DEPOIS: ", valores)

print("-" * 40)  # Traço de 40 hífens

# 8) removendo um elemento por sua posição:  pop() com parâmetro
removido = valores.pop(3) #remove o elemento da posição 3 
print("valor removido da posição 3: ", removido)
print(valores)
removido = valores.pop(0)  # remove o primeiro elemento
print("valor removido da primeira posição: ", removido)
print(valores)

print("-" * 40)  # Traço de 40 hífens

#9) removendo um elemento pelo seu valor: remove()
print("antes: ", legumes)
legumes.remove("abobrinha")
print("após a remoção de abobrinha: ", legumes)

print("-" * 40)  # Traço de 40 hífens

# Acrescentando alguns legumes para aumentar a lista
legumes.append("beterraba")
legumes.append("abobrinha")
legumes.append("batata doce")
legumes.append("mandioquinha")
legumes.append("cará")
legumes.append("nabo")

#10) Fatiando uma lista
#    fatiar significa copiar uma parte da lista (uma sublista) para uma nova lista

print(legumes)

# cria uma sublista que contém os elementos da posição 2 até a posição 7
#  (posição 8 NÃO entra)
sublista2_7 = legumes[2:8]
print("Sublista de 2 a 7: ", sublista2_7)

# cria uma sublista que contém os elementos do início até a posição 5
# (posição 6 NÃO entra )
sublista0_5 = legumes[:6]
print("Sublista de 0 a 5: ", sublista0_5)

# cria uma sublista que contém os elementos da posição 8 até o final
sublista8_fim = legumes[8:]
print("sublista do 8 até o final: ", sublista8_fim)

