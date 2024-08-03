vendas = 1500
meta = 1300 


if vendas > meta:
    print("Vendedor ganha bônus")
    print("Bateu a meta de venda")
    bonus = 0.1 * vendas
    print("Bônus do vendedor: ", bonus)
else: 
    print("Vendedor não ganha bônus")
    print("Não bateu a meta de vendas")


# Segundo cenário

vendas = 1500
vendas_empresa = 10000
meta_empresa = 20000
meta1 = 1300 # ganhar 10%
meta2 = 2000 # ganhar 13%

if vendas >= 2000 and vendas_empresa >= meta_empresa:
    bonus = 0.13 * vendas
else:
    if vendas >= 1300 and vendas_empresa >= meta_empresa:
        bonus = 0.1 * vendas
    else:
        bonus = 0

print("Bônus: ", bonus)

lista_produtos = ["airpod", "ipad", "iphone", "macbook", ]
produto_procurado = input("procure um produto: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print("Produto no estoque")
else:
    print("Produto sem estoque")


