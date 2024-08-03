# inputs
#email = input("Escreva seu e-mail: ")
#nome = input ("Seu primeiro nome: ")


#print(f"{nome}, verifique seu email {email}, enviamos um link de confirmação")


#faturamento = float(input("Digite seu faturamento: "))

#imposto = faturamento * 0.1
#print(imposto)

# listas

vendas = [100, 50, 14, 20, 30, 700]

# soma dos elementos
total_vendas = sum(vendas)

print (total_vendas)

# tamanho da lista

quantidade_vendas = len(vendas)
print(quantidade_vendas)

# max e min
print(max(vendas))
print(min(vendas))

# pegar posição
print(vendas[-1])

lista_produtos = ["iphone", "airpod", "ipad", "macbook"]

produto_procurado = input("Pesquise pelo nome do produto: ")
produto_procurado = produto_procurado.lower()

print(produto_procurado in lista_produtos)


# adicionar um item
lista_produtos.append("apple watch")
print(lista_produtos)

# remover um item
lista_produtos.remove("ipad")    # remove voce passa o NOME do item que voce quer remover da lista
print(lista_produtos)

lista_produtos.pop(0)                   # pop voce passa a POSICAO do item DA LISTA que voce quer remover da lista
print(lista_produtos)

# editar um item
preços = [1000, 1500, 3500]
preços[0] = 6000 + 1000
print(preços)

# contar quantas vezes um item aparece na lista
lista_produtos = ["iphone", "airpod", "ipad", "macbook", "iphone", "ipad", "iphone"]

print(lista_produtos.count("iphone"))

# ordenar lista
lista_produtos.sort()
print(lista_produtos)

vendas.sort()
print(vendas)
