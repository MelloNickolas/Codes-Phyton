# Vamos realizar um código onde você poderá criptografar e descriptografar uma mensagem

def criptografar():
# criando uma lista para armazenar o texto criptografado
  txtCriptografado = []

# o replace(" ", "") vai garantir que a nossa cripto vai ler apenas as letras e esquecer os espaços
# upper() converte todas as letras para maiusculas, porque Vigenere só usa maiusculas.

# msg é o texto que será criptografado
msg = msg.replace(" ", "").upper()
#  Aqui que vamos colococar a chave para realizar a cifra de vigenere, para assim criptografar usando a grade de vigenere
key = key.replace(" ", "").upper()

# Essa variavel vai controlar como nos vamos usar na grade de vigenere
key_grade = 0

# for vai iterar sobre cada letra da msg.
# len(msg) vai mostrar o numero de caracteres da mensagem.
# range vai pegar a quantidade de letras do len e usar ele para acessar e criptografar as letras da mensagem
for i in range(len(msg)):

  # lembra que usamos o i no for para passar por cada letra, aqui estamos armazezando elas em uma variavel a cada iteracao
  letra_msg = msg[i]

  # Aqui vamos verificar se os caracteres inseridos são letras, isso é importante pq vigenere so trabalaha com letras
  if letra_msg.isalpha():
