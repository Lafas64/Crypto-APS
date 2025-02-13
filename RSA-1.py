import random
import math

textnum = []
textnum_cript = []
textof = ''
d = e = p = q = None


# Gera um número primo até o número estabelecido pela variável primos
def sort_primo(num):
    prime_num1 = []
    prime_num2 = [True] * (num + 1)
    for i in range(2, num + 1):
        if prime_num2[i]:
            prime_num1.append(i)
            for j in range(2, int(num / i) + 1):
                prime_num2[i * j] = False
    return prime_num1


def num_random_int(min, max):
    min = math.ceil(min)
    max = math.floor(max)
    return math.floor(random.random() * (max - min + 1)) + min


primos = sort_primo(300)  # Define o limite dos números primos


# Função mdc (Máximo Divisor Comum)
def mdc(x, y):
    while y:
        t = y
        y = x % y
        x = t
    return x


# Função mmi
def mmi(a, z):
    for x in range(1, z):
        if ((a % z) * (x % z)) % z == 1:
            return x


# Função para gerar a chave pública e privada
def generate_keys(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    e = 0
    temp = num_random_int(1, z)
    while e == 0:
        tempE = mdc(temp, z)
        if tempE == 1:
            e = temp
        else:
            temp = num_random_int(1, z)
    d = mmi(e, z)
    return e, d, n


def encrypt_message(textnum, e, n):
    textnum_cript = []
    for numero in textnum:
        textnum_cript.append((numero ** e) % n)
    return textnum_cript


def decrypt_message(textnum, d, n):
    textnum_cript = []
    for numero in textnum:
        textnum_cript.append((numero ** int(d)) % int(n))
    return textnum_cript


# Opções de criptografia
resp = input(
    'Você deseja \033[31mCriptografar\033[m ou \033[34mDescriptografar\033[m uma mensagem? [\033[31m1\033[m/\033[34m2\033[m]  ').strip().upper()
while resp not in ['CRIPTOGRAFAR', 'DESCRIPTOGRAFAR', '1', '2']:
    resp = input(
        'Você deseja \033[31mCriptografar\033[m ou \033[34mDescriptografar\033[m uma mensagem? [\033[31m1\033[m/\033[34m2\033[m] ').strip().upper()

if resp == 'CRIPTOGRAFAR' or resp == "1":  # Escolha para criptografar
    frase = str(input('Qual mensagem você deseja \033[31mCriptografar\033[m? '))
    for letra in frase:
        textnum.append(ord(letra))

    escolhaKey = int(input(
        'Você deseja \033[31mescolher os números para gerar a chave\033[m ou gerar uma \033[34mchave aleatoria\033[m? [\033[31m1\033[m/\033[34m2\033[m] '))

    if escolhaKey == 1:
        p = int(input('Escolha um número primo (que seja pelo menos maior que 11) para a chave P: '))
        while p <= 10:
            p = int(input('Escolha um número primo (que seja pelo menos maior que 11) para a chave P: '))
        q = int(input('Escolha outro número primo (que seja pelo menos maior que 11) para a chave Q: '))
        while q <= 10:
            q = int(input('Escolha outro número primo (que seja pelo menos maior que 11) para a chave Q: '))
        e, d, n = generate_keys(p, q)
        print(f'Texto convertido para número: \n{textnum}')

        textnum_cript = encrypt_message(textnum, e, n)

        print(f'Texto numérico criptografado: \n{textnum_cript}')

        for numero in textnum_cript:
            textof += chr(numero)
        print(f'Texto \033[31mCriptografado\033[m: {textof}')
        print(f'Chave de \033[34mDescriptografia\033[m: {d}/{n}')

    elif escolhaKey == 2:
        p = primos[num_random_int(len(primos) - 60, len(primos))]
        q = primos[num_random_int(len(primos) - 60, len(primos))]
        e, d, n = generate_keys(p, q)

        print(f'Texto convertido para número: \n{textnum}')

        textnum_cript = encrypt_message(textnum, e, n)

        print(f'Texto numérico criptografado: \n{textnum_cript}')

        for numero in textnum_cript:
            textof += chr(numero)
        print(f'Texto \033[31mCriptografado\033[m: {textof}')
        print(f'Chave de \033[34mDescriptografia\033[m: {d}/{n}')

elif resp == 'DESCRIPTOGRAFAR' or resp == "2":  # Escolha para descriptografar
    cifra = input('Qual mensagem você deseja \033[34mDescriptografar\033[m? ')
    chave = str(input('Digite a chave de \033[34mDescriptografia\033[m: ')).split('/')
    d = chave[0]
    n = chave[1]

    for letra in cifra:
        textnum.append(ord(letra))
    print(f'Texto convertido para número: \n{textnum}')

    textnum_cript = decrypt_message(textnum, d, n)

    for numero in textnum_cript:
        textof += chr(numero)
    print(f'Texto \033[34mDescriptografado\033[m: {textof}')
