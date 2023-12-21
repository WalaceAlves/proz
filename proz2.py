
nome = input("Informe seui nome completo: ")
ano_nascimento = int(input("Informe seu ano de nascimento. "))
idade_atual = 2022 - ano_nascimento  
if ano_nascimento < 1922 or ano_nascimento > 2021:   
    try print("Digite outro ano")
else:
    print(idade_atual)                