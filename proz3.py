# Importa a biblioteca para tratar erros
import re

# Declara as variáveis
nome = ""
ano_nascimento = 0

# Recebe o nome do usuário
print("Qual é o seu nome?")
nome = input()

# Valida o nome do usuário
while not nome.isalpha():
    print("O nome deve ser composto apenas por letras.")
    print("Qual é o seu nome?")
    nome = input()

# Recebe o ano de nascimento do usuário
print("Qual é o seu ano de nascimento?")
ano_nascimento = input()

# Valida o ano de nascimento do usuário
while not re.match("[0-9]{4}", ano_nascimento):
    print("O ano de nascimento deve ser um número de 4 dígitos.")
    print("Qual é o seu ano de nascimento?")
    ano_nascimento = input()

# Calcula a idade do usuário
idade = 2022 - int(ano_nascimento)

# Exibe o resultado
print(f"Olá, {nome}! Você tem {idade} anos.")
