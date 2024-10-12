# Vamos realizar um código onde você poderá criptografar e descriptografar uma mensagem



def descriptografar(msg, key):
  # criando uma lista para armazenar o texto criptografado
  txtDescripto = []

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
  # range vai pegar a quantidade de letras do len - 1 e usar ele para acessar e criptografar as letras da mensagem
  for i in range(len(msg)):

    # lembra que usamos o i no for para passar por cada letra, aqui estamos armazezando elas em uma variavel a cada iteracao
    letra_msg = msg[i]

    # Aqui vamos verificar se os caracteres inseridos são letras, isso é importante pq vigenere so trabalaha com letras
    if letra_msg.isalpha():

      # ORD Quando você passa um caractere para ord(), ele converte esse caractere para seu equivalente numérico baseado na tabela Unicode. 
      # Cada caractere, como letras, números e símbolos, tem um número único que o representa no padrão Unicode.
      # Estamos convertendo cada letra da mensagem em um número subtraindo A na tabela UniCode. Exemplo:
      #  Se letra_msg for 'C', então ord('C') - ord('A') = 67 - 65 = 2.
      letra_msg_num = ord(letra_msg) - ord('A')

      # key[key_grade]: Obtém o caractere atual da chave usando key_grade como índice.
      # ord(key[key_grade]) - ord('A'): Converte essa letra em seu valor numérico, que nem explicado ali em cima.
      # Essas duas variaveis serviram para armazenar nossa letra como numero.
      letra_key_num = ord(key[key_grade]) - ord('A')

      # Aqui estamos aplicando a formula dde descriptografia da cifra de vigenere
      # o % 26 serve para garantir que o resultado esteja dentro do intervalo de 26 letras.
      # Exemplo: Se letra_msg_num = 4 (E) e letra_key_num = 3 (D), então (4 - 3) % 26 = 1, que corresponde à letra 'B'.
      letra_descripto_num = (letra_msg_num - letra_key_num) % 26

      # letra_descripto_num + ord('A'):
      # Soma o valor numérico com o código Unicode da letra 'A' para obter o código Unicode da letra correspondente.
      # chr(...): Converte o código Unicode de volta para o caractere.
      # Exemplo: Se letra_descripto_num = 1, então chr(1 + 65) = chr(66) = 'B'.
      letra_descripto = chr(letra_descripto_num + ord('A'))

      #Aqui ele vai adicionando as letras descriptografadas para o fim da lista.
      txtDescripto.append(letra_descripto)

      # (key_grade + 1) incrementa o indice na chave para passar para a proxima letra\
      # % len(key)  Aplica o operador módulo para que, quando o fim da chave for alcançado, o índice retorne ao início (0).
      # Exemplo: Se a chave tem comprimento 4 e key_index era 3, então (3 + 1) % 4 = 0, reiniciando a chave.
      key_grade = (key_grade + 1) % len(key)

    # Aqui estamos colocando os caracteres que nao sao letras, ou seja, espaços, numeros e pontuações.
    else:
      # adiciona a lista a letra
      txtDescripto.append(letra_msg)

  #Produzindo a mensagem final como uma String
  return ''.join(txtDescripto)

#Agora vamos colocar a funçao para criptografar a nossa msg.
def criptografar(msg, key):
  txtCripto = []
  msg = msg.replace(" ", "").upper()
  key = key.replace(" ", "").upper()

  key_grade = 0

  for i in range(len(msg)):
    letra_msg = msg[i]
    if letra_msg.isalpha():
      letra_msg_num = ord(letra_msg) - ord('A')
      letra_key_num = ord(key[key_grade]) - ord ('A')
      #Aqui so inverteremos o sinal pois estamos criptografando, ou seja é o inverso
      letra_cripto_num = (letra_msg_num + letra_key_num) % 26
      letra_cripto = chr(letra_cripto_num + ord('A'))
      txtCripto.append(letra_cripto)
      key_grade = (key_grade + 1) % len(key)
    else:
      txtCripto.append(letra_msg)

  return ''.join(txtCripto)

def userface():
  print(" Escolha uma das opcções : ")
  print()
  print("  Criptografar   == 1 ")
  print(" Descriptografar == 2")
  print()
  opcao = input(" Qual a sua escolha ? ")

  if opcao not in ['1', '2']:
    print(" Opção Inválida, favor seguir as opções mostradas ")
    return

  msg = input("\n Digite a mensagem : ")
  key = input(" Digite a chave fornecida : ")

  if opcao == '1':
    msg_cripto = criptografar(msg, key)
    print(f"\n Mensagem Criptografada == {msg_cripto}")
  elif opcao == '2':
    msg_descripto = descriptografar(msg, key)
    print(f"\n Mensagem Descriptografada == {msg_descripto}")

if __name__ == "__main__":
  userface()