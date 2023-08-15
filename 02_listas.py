# LISTAS
#Listas são uma forma de armazenar mais de uma única variável. Os valores podem ser de tipos diferentes.

# Uma lista de números
valores = [2,3,5,7,9,11]

# Uma lista com valores de tipos variados
legumes = ["batata","tomate","abobrinha","beterraba"], 

# OPERÇÕES SOBRE LISTAS
#1) PERCURSO: significa percorrer a lista do primeiro ao último elemento, fazendo algo a cada um deles.

#Imprimindo cada um dos elementos da lista, um por linha:
for val in valores:
    print(val)

print("-"*48) # traço de 48 hifens

#imprimimndo o dobro do valor de cada elemento da lista
for x in valores:
    print(x * 2)

#2) INSERINDO UM NOVO VALOR NO *FIM* DA LISTA

valores.append(13)
legumes.append("Cebola")

print(valores)
print(legumes)

print("-"*48)
# 2°: o novo elemento a ser inserido

legumes.insert(2, "mandioquinha")
print(legumes)
legumes.insert(0, "beterraba")
print(legumes)

print("-" * 48)

#4) ACRESCENTANDO O VALOR A UMA POSIÇÃO ESPECÍFICA
print("Elemento na QUARTA posição:", valores[3])
print("Elemento na PRIMEIRA posição: ", valores[8])
print("elemento na ÚLTIMA posição:", valores [-1])
print("Elemento na PENÚLTIMA posição: ", valores [-2])

