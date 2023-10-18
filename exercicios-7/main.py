def saudacao(nome):
    return f'Olá, {nome}!'

def dobro(num):
    return num * 2

def saudacao_personalizada(nome, idioma = 'inglês'):
    if idioma == 'inglês':
        return f'Hello, {nome}!'
    elif idioma == 'espanhol':
        return f'Hola, {nome}!'
    elif idioma == 'francês':
        return f'Bonjour, {nome}!'

def potencia(base, expoente = 2):
    return base ** expoente

def idade_valida(idade):
    return idade >= 0 and idade <= 150

def validar_email(email):
    if ' ' in email:
        return False
    if '@' not in email:
        return False
    if email.endswith('@.com'):
        return False
    if not email.endswith('.com'):
        return False
    return True

def calcular_pagamento(horas_trabalhadas, taxa_hora):
    return horas_trabalhadas * taxa_hora

def maior_numero(a, b, c):
    return max_custom([a, b, c])

def contagem_letras(palavra):
    total_maiuscula = 0
    total_minuscula = 0

    for letra in palavra:
        if letra in 'abcdefghijklmnopqrstuvwxyz':
            total_minuscula += 1
        elif letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            total_maiuscula += 1
    
    return (total_maiuscula, total_minuscula)

def len_custom(iteravel):
    contagem = 0
    for _ in iteravel:
        contagem += 1
    return contagem

def sum_custom(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

def max_custom(lista):
    maior = None

    for numero in lista:
        if maior is None or numero > maior:
            maior = numero

    return maior

def min_custom(lista):
    menor = None

    for numero in lista:
        if menor is None or numero < menor:
            menor = numero

    return menor

def startswith_custom(string, prefixo):
    indice = 0
    for caractere in prefixo:
        if caractere != string[indice]:
            return False
        indice += 1
    return True

def endswith_custom(string, prefixo):
    indice = len_custom(string) - 1
    for caractere in reversed(prefixo):
        if caractere != string[indice]:
            return False
        indice -= 1
    return True

def split_custom(string, caractere):
    resultado = []

    parte = ''
    for letra in string:
        if letra != caractere:
            parte += letra
        else:
            resultado.append(parte)
            parte = ''
    resultado.append(parte)
    parte = ''

    return resultado

def strip_custom(string, caracteres_remover):
    resultado = string
    while True:
        if startswith_custom(resultado, caracteres_remover):
            resultado = resultado[1:]
        elif endswith_custom(resultado, caracteres_remover):
            resultado = resultado[:-1]
        else:
            break

    return resultado

def replace_custom(string, substring_antiga, substring_nova):
    pedacos_da_string = string.split(substring_antiga)
    resultado_em_pedacos = []
    print(pedacos_da_string)

    for i in range(len_custom(pedacos_da_string)):
        resultado_em_pedacos.append(pedacos_da_string[i])
        if i != len_custom(pedacos_da_string) - 1:
            resultado_em_pedacos.append(substring_nova)
    resultado = ''
    for pedaco in resultado_em_pedacos:
        resultado += pedaco

    return resultado
