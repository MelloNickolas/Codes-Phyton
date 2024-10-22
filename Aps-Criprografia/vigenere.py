def descriptografar(msg, key):
  txtDescripto = []
  msg = msg.upper()
  key = key.upper()
  key_grade = 0

  for i in range(len(msg)):
    letra_msg = msg[i]

    if letra_msg.isalpha():
      letra_msg_num = ord(letra_msg) - ord('A')
      letra_key_num = ord(key[key_grade]) - ord('A')
      letra_key_num = ord(key[key_grade]) - ord('A')
      letra_descripto_num = (letra_msg_num - letra_key_num) % 26
      letra_descripto = chr(letra_descripto_num + ord('A'))
      txtDescripto.append(letra_descripto)
      key_grade = (key_grade + 1) % len(key)

    else:
      txtDescripto.append(letra_msg)

  return ''.join(txtDescripto)


def criptografar(msg, key):
  txtCripto = []
  msg = msg.upper()
  key = key.upper()
  key_grade = 0

  for i in range(len(msg)):
    letra_msg = msg[i]
    if letra_msg.isalpha():
      letra_msg_num = ord(letra_msg) - ord('A')
      letra_key_num = ord(key[key_grade]) - ord ('A')
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