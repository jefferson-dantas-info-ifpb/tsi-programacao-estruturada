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
    return max(a, b, c)

def contagem_letras(palavra):
    totalMaiuscula = 0
    totalMinuscula = 0

    for letra in palavra:
        if letra in 'abcdefghijklmnopqrstuvwxyz':
            totalMinuscula += 1
        elif letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            totalMaiuscula += 1
    
    return (totalMaiuscula, totalMinuscula)

def len_custom(iteravel):
    return len(iteravel)

def sum_custom(lista):
    return sum(lista)

def max_custom(lista):
    if len(lista) != 0:
        return max(lista)

def min_custom(lista):
    if len(lista) != 0:
        return min(lista)

def startswith_custom(string, prefixo):
    return string.startswith(prefixo)

def endswith_custom(string, prefixo):
    return string.endswith(prefixo)

def split_custom(string, caractere):
    return string.split(caractere)

def strip_custom(string, caracteres_remover):
    return string.strip(caracteres_remover)

def replace_custom(string, substring_antiga, substring_nova):
    return string.replace(substring_antiga,substring_nova)
