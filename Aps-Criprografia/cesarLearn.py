# vamos definir apenas uma funçao tanto para criptografia, quanto para descriptografar
# será definido qual vai usar na userface, onde o usuário vai definir qual usar.

# txt é o texto que o usuário informará
# key é o numero que o user vai informar, que será a quantidade casas pra frente que pulará
# exemplo= se txt = A e a key = 2 o novo texto será = C
# funcao sera onde ele deseja CRIPTOGRAFAR = 1 ou DESCRIPTOGRAFAR = -1
# Mais pra frente voces vao entender o pq disso
def cripto_decripto(txt, key, funcao):

  # Criando uma variavel onde a gente vai armazenar a nova msg
  resultado = ""

  # Loop para rodar em cada letra do texto
  for letra in txt:
    # Verificando se os caracteres são letras
    if letra.isalpha():

      # Aqui nos estamos definindo um limite, pois vamos mudar as letras para os número ASCII.
      # Se a letra for maiúscula (letra.isupper()), o ponto de partida é o código ASCII de 'A' (65).
      # Se a letra for minúscula, o ponto de partida é o código ASCII de 'a' (97).
      limite = 65 if letra.isupper() else 96

      # Estamos realizando tudo nessa linha
      # ord(letra) Esta -- convertendo a ltra da mensagem em um numero
      # ord(letra) - limite -- normaliza os valores da letra para 0, lembra que se for minuscula muda
      # mas se for maisucula vai ser outro valor valor por isso fizemos aquele limite, pq agora em ambas as letras vai ser 0
      # (key * funcao) -- lembra que eu falei que agora voce vai entender o porque CRIPTOGRAFAR = 1 e DESCRIPTOGRAFAR = -1
      # isso se deve a essa parte pois se a chave for 7, se for para CRIPTOGRAFAR ele vai continuar 7 e andar 7 casas para a frente
      # Porem se for5 para descriptografar vai multiplicar por -1 entao ficará -7 andando 7 casas para trás.
      # %26 -- tamo garantindo que vai estar dentro das 26 letras do alfabeto
      # chr(... + limite) -- Aqui estamos convertendo o valor para uma letra de novo, lembra que o limite usamos para zerar?, 
      # Aqui vamos voltar ela para o valor inicial se for maiuscula vai ter um valor e se for minuscula vai ter outro valor.
      # EXEMPLO: se tiver a letra 'A' e 'a' o valor de ambas vai ser 0 + o limite 'A' + 65 e 'a' + 97, devido ao limite que
      # colocamos lá em cima, ai o chr vai usar o código ASCII para voltar a letra inicial.
      letraNova = chr((ord(letra) - limite + (key * funcao)) % 26 + limite)

      # aqui estamos adicionando a nova letra a nossa mensagem nova
      resultado += letraNova

    # Aqui vamos pegar tudo que nao é letra ou seja numeros e espacos e adiciona-los a mensagem como a mesma coisa
    # sem modificar em nada.
    else:
      resultado += letra

  return resultado


def userface():
  

  print(" \n Escolha uma das opcções : ")
  print()
  print("  Criptografar   == 1 ")
  print(" Descriptografar == 2")
  print()
  funcao = input(" Qual a sua escolha ? ")


  if funcao not in ['1', '2']:
    print(" Opção Inválida, favor seguir as opções mostradas ")
    return
  
  txt = input(" \n Informe a mensagem : ")
  key = int(input(" Informe o número da codificação : "))

  #Aqui estamos vendo se o user escolheu criptografar, vamos passar os parametros como
  # o txt que o user digitou a key, e a funcao vai ser 1, pois lá em cima na outra funçao
  # nos vamos multiplicar a chave lembra?
  # A mesma coisa vai ser se ele vai descriptografar ai vai multiplicar por -1.
  if funcao == '1':
    print("\n Fras Criptografada : ", cripto_decripto(txt, key, 1))
  elif funcao == '2':
    print("\n Fras Criptografada : ", cripto_decripto(txt, key, -1))

  else:
    print("Opção inválida!")

# Rodando o nosso programaS 
if __name__ == "__main__":
  userface()