# 1) (0,5) Faça um programa que armazene dados de produtos em uma lista, com a seguinte
# estrutura:
# a. Código
# b. Nome
# c. Estoque
# d. Estoque mínimo
# e. Estoque máximo
# f. Preço de custo
# g. Preço de venda
# h. Porcentagem de ICMS
# i. Porcentagem de IPI
# Requisitos:
# • Gere os dados automaticamente (fakes), exemplo:
# o Código: 12 (random)
# o Nome: Produto 12
# o Estoque: 55.0 (random)
# • Não permita que o estoque máximo seja menor que o estoque mínimo
# • Não permita valores negativos para os campos: estoque, preço de custo, preço de venda, ICMS e IPI.

import random

# vamos gerar os dados dos produtos aleatórios
def produto_dados_ale(codigo):

# Aqui estamos puxando qual é o código que geramos aleatoriamente na funçao abaixo. 
  nome = f"Produto {codigo}"

# Aqui a função ROUND q serve para arredonda um numero FLOAT(numero com virgula), para um numero especifico com casas decimais
# O RANDOM.UNIFORM serve para gerar um numero aleatório dentre um (valor-MIN, valor-MAX)
# já o ,2 serve para definir quantas casas decimais o seu número vai ter.
  estoque = round(random.uniform(1, 100))

# Aqui estamos mostrando que o estoque minimo deve ser 1 e o máximo deve ser o que tem no estoque.
  estoque_min = round(random.uniform(1, estoque))
  estoque_max = round(random.uniform(estoque, 999))
  preco_custo = round(random.uniform(0.1, 9999), 2)
  preco_venda = round(random.uniform(preco_custo, preco_custo + 999), 2)
  icms = round(random.uniform(1, 50), 0)
  ipi = round(random.uniform(1, 50), 0) 

# Garantindo que o estoque maximo não vai ser menor que o estoque minimo
  if estoque_max < estoque_min:
    estoque_max = round(estoque_min + random.uniform(1, 999)) 

  lucro_bruto = preco_venda - preco_custo
  lucro = round(lucro_bruto, 2)

# retornando uma lista
  return {
    "Códigos": codigo,
    "Nome": nome,
    "Estoque": estoque,
    "Estoque Mínimo": estoque_min,
    "Estoque Máximo": estoque_max,
    "Preço de Custo": preco_custo,
    "Preço de Venda": preco_venda,
    "Porcentagem de ICMS": icms,
    "Porcentagem de IPI": ipi,
    "Lucro": lucro
  }

# gerando a quantidade de produtos que vai gerar, e puxando os dados gerando anteriormente
def gerar_produtos(total_prod):

  # gerando a lista para armazenar os dados aleatorios dos produtos que forem gerados.
  produtos = []

  # aqui vamos gerar um código de 1 até o num_produtos que ainda nao foi definido
  # esse +1 que está ai é para gerar produtos de 1 até num_produtos, é necessário adicionar 1 ao valor de num_produtos.
  for codigo in range(1, total_prod + 1):

  # aqui fala que o produto vai ser igual aos dados gerado la na funçao de cima
    produto = produto_dados_ale(codigo)
  # e aqui estamos adicionando o produto a lista de produtos
    produtos.append(produto)

  return produtos

def prints(produtos):

  for produto in produtos:

    print()
    print("---------------------------------------------------------------------")
    print("Produto Código: -- ", produto["Códigos"])
    print("Nome: -- ", produto["Nome"])
    print("Estoque: -- ", produto["Estoque"])
    print("Estoque Mínimo: -- ", produto["Estoque Mínimo"])
    print("Estoque Máximo: -- ", produto["Estoque Máximo"])
    print("Preço de Custo: -- R$", produto["Preço de Custo"])
    print("Preço de Venda: -- R$", produto["Preço de Venda"])
    print("Porcentagem de ICMS: -- ", produto["Porcentagem de ICMS"], "%")
    print("Porcentagem de IPI: -- ", produto["Porcentagem de IPI"], "%")
    print("Lucro: -- R$", produto["Lucro"])
    print("---------------------------------------------------------------------")
    print()


def valores_max_min(produtos):

  maior_preco = max(produtos, key=lambda m: m['Preço de Venda'])
  menor_preco = min(produtos, key=lambda m: m['Preço de Venda'])
  maior_estoque = max(produtos, key=lambda m: m['Estoque'])
  menor_estoque = min(produtos, key=lambda m: m['Estoque'])
  maior_icms = max(produtos, key=lambda m: m['Porcentagem de ICMS'])
  menor_icms = min(produtos, key=lambda m: m['Porcentagem de ICMS'])
  maior_lucro = max(produtos, key=lambda m: m['Lucro'])
  menor_lucro = min(produtos, key=lambda m: m['Lucro'])

  print()
  print(f"Produto de maior PREÇO -- {maior_preco['Nome']} -- R$ {maior_preco['Preço de Venda']}")
  print(f"Produto de menor PREÇO -- {menor_preco['Nome']} -- R$ {menor_preco['Preço de Venda']}")
  print(f"Produto com o maior ESTOQUE -- {maior_estoque['Nome']} -- {maior_estoque['Estoque']}")
  print(f"Produto com o menor ESTOQUE -- {menor_estoque['Nome']} -- {menor_estoque['Estoque']}")
  print(f"Produto com o maior ICMS -- {maior_icms['Nome']} -- {maior_icms['Porcentagem de ICMS']}%")
  print(f"Produto com o menor ICMS -- {menor_icms['Nome']} -- {menor_icms['Porcentagem de ICMS']}%")
  print(f"Produto com o maior LUCRO -- {maior_lucro['Nome']} -- R$ {maior_lucro['Lucro']}")
  print(f"Produto com o menor LUCRO -- {menor_lucro['Nome']} -- R$ {menor_lucro['Lucro']}")





if __name__ == "__main__":
    produtos = gerar_produtos(5)
    prints(produtos)
    valores_max_min(produtos)