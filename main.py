import random
import string

# Solicita o nome do usuário
nome = input("Digite seu nome: ")

# Listas de caracteres
letras = string.ascii_lowercase  # letras minúsculas
numeros = string.digits          # números de 0 a 9
simbolos = ['@', '#', '%', '&']  # símbolos permitidos

# Seleciona os caracteres aleatórios
part_letras = ''.join(random.choice(letras) for _ in range(3))
part_numeros = ''.join(random.choice(numeros) for _ in range(3))
part_simbolos = ''.join(random.choice(simbolos) for _ in range(2))

# Junta todas as partes e embaralha
senha_lista = list(part_letras + part_numeros + part_simbolos)
random.shuffle(senha_lista)
senha = ''.join(senha_lista)

# Exibe o resultado
print(f"Olá, {nome}! Sua senha segura é: {senha}")
