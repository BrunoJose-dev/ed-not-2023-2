# # função que calcula o imc de uma pessoa
# def calc_imc(peso, altura): # def signfica uma função em python, é o nome que será utilizado para chamar a função
#     return peso / altura ** 2  # return signifa a formula que será repetida na função

# p = 85
# a = 1.72
# imc = calc_imc(p, a) #Os valores devem ser passados em ordem, ex: o p deve ir 1° porque a formula está com o peso 1°

# print(imc)

# print(calc_imc(85, 1.72)) #O print já recebe os valores da variáveis, chama a função e mostra o resusltado. Tem a possibilidade de fazer tudo dentro do print
 
 ####################################################################

from math import pi

"""
   função que calcula a área de uma figura plana
"""
def calc_area(base, altura, tipo):
    
    resultado = None  # Valor não existente (com V maiúsculo)
    
    if tipo == "R":    #Retângulo 
        resultado = base * altura
    
    elif tipo == "T": #Triângulo#
        resultado = base * altura/2
    
    elif tipo == "E":  #Elipse
        resultado = (base/2) * (altura/2) * pi
    
    else:    #Forma inválida ou desconhecida
        resultado = None
    
    return resultado

print ("Retângulo 20 x 30 ", calc_area(20, 30, "R"))
print ("triângulo 45 x 32 ", calc_area(45, 32, "T"))
print ("Elipse 10 x 15 ", calc_area(10, 15, "E"))
print ("Desconhecido 12 x 16 ", calc_area(12, 16, "D"))
