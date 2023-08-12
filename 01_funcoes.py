# função que calcula o imc de uma pessoa
def calc_imc(peso, altura): # def signfica uma função em python, é o nome que será utilizado para chamar a função
    return peso / altura ** 2  # return signifa a formula que será repetida na função

# p = 85
# a = 1.72
# imc = calc_imc(p, a) #Os valores devem ser passados em ordem, ex: o p deve ir 1° porque a formula está com o peso 1°


# print(imc)
print(calc_imc(85, 1.72))