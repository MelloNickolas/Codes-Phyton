# Faça um programa para gerar automaticamente números entre 0 e 99 de uma cartela de
# bingo. Sabendo que cada cartela deverá conter 5 linhas de 5 números, gere estes dados de modo a
# não ter números repetidos dentro das cartelas. O programa deve exibir na tela a cartela gerada de
# acordo com a imagem abaixo: 

# Importando a biblioteca
import random

def gerar():
# gera 25 numeros de 0 a 99
  numeros = random.sample(range(100), 25)

# range(start, stop, step)
# start: o número inicial da sequência (inclusive).
# stop: o número final da sequência (não inclusive).
# step: o intervalo entre os números (ou o "passo").
# LEMBRANDO QUE ELE NAO MOSTRA O ULTIMO NUMERO DA SEQUENCIA EX:
# range(0, 25) 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24 e o 25 nao ira entrar
# range(10, 2, -2) 10,8,6,4 e 2 não entra no range

  cartela = [numeros[i:i+5] for i in range(0, 25, 5)]
# numeros[i:i+5] aqui estamos fatiando a tabela em um indice especifico de 5, so estamos fazendo isso
# porque geramos 25 numeroes, ou seja ele se formara em 25 linhas.
# for i in range(0, 25, 5) 
# fatiar a lista numeros em grupos de 5 números. Cada valor de i define o índice inicial de cada grupo de 5 números consecutivos.

  cartela[2][2] = "Michael Jackson"
# coloquei o nome no meio da cartela [linhas][colunas]

  return cartela


def exibir(cartela):
  for linha in cartela:
    print(" | ".join(f"{num:2}" for num in linha))
    print("-" * 21)

# for linha in cartela: aqui o for vai percorrer a variavel linha da cartela
# A variável linha será, a cada iteração, uma lista que representa uma linha da cartela de bingo.

#  join() é usada para concatenar (juntar) elementos de uma lista ou outro iterável em uma única string, com um separador entre os elementos.

# O f"{num:2}" significa que o número num (que será um dos números da linha) será convertido para uma string com pelo menos 2 caracteres de largura.
# Ou seja, se o número tiver apenas um dígito (como 1 ou 7), ele será exibido com um espaço à esquerda, garantindo que todos os números na linha fiquem alinhados de forma mais organizada.

# O "-" * 21 cria uma string com 21 caracteres de traço. Isso ajuda a separar cada linha de números de forma clara, criando um estilo de tabela visual.

# definindo e gerando a nossa tabela
cartela = gerar()
exibir(cartela)