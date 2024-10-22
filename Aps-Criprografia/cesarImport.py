def cripto_decripto(txt, key, funcao):
  resultado = ""
  for letra in txt:
    if letra.isalpha():
      limite = 65 if letra.isupper() else 97
      letraNova = chr((ord(letra) - limite + (key * funcao)) % 26 + limite)
      resultado += letraNova
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
  
  arquivo = "./msg.txt"

  try:
    # 'r' (modo de abertura): O argumento 'r' significa que o arquivo será aberto em modo leitura (read)
    with open(arquivo, 'r') as file:
      txt = file.read()
  except FileNotFoundError:
    print("Arquivo não encontrado")
    return
  key = int(input(" Informe o número da codificação : "))

  if funcao == '1':
    print("\n Fras Criptografada : ", cripto_decripto(txt, key, 1))
  elif funcao == '2':
    print("\n Fras Criptografada : ", cripto_decripto(txt, key, -1))
  else:
    print("Opção inválida!")

if __name__ == "__main__":
  userface()