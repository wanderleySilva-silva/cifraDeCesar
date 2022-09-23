
from ast import IsNot
import sys

MODO_ENCRIPTAR = 1
MODO_DECRIPTAR = 0

def cesar(dados, chave, modo):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.'

    novo_dado = ''

    for c in dados:
        index = alfabeto.find(c)

        if c not in alfabeto:
            print('Caractere não pertence ao alfabeto.')
            sys.exit()
        else:
            if index == -1:
                novo_dado += c
            else:
                novo_index = index + chave if modo == MODO_ENCRIPTAR else index - chave
                novo_index = novo_index % len(alfabeto)
                novo_dado += alfabeto[novo_index:novo_index+1]
    return novo_dado

chave = int(input('Digite o tamanho da chave: '))

texto_original = input('Digite um texto: ')
print('Texto original: ', texto_original)

texto_cifrado = cesar(texto_original,chave,MODO_ENCRIPTAR)
print('Texto encriptado: ', texto_cifrado)

texto_decriptado = cesar(texto_cifrado,chave,MODO_DECRIPTAR)
print('Texto decriptado: ', texto_decriptado)

    



            