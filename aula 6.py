lista_produtos = ["airpod", "ipad", "iphone", "macbook"]
precos = [2000, 9000, 6000, 11000]
          
dic_produtos = {"airpod": 2000, "ipad": 9000, "iphone": 6000, "macbook": 11000}

# pegar um elemento
print(dic_produtos["iphone"])

# editar um elemento
dic_produtos["iphone"] = dic_produtos["iphone"] * 1.3
print(dic_produtos)

# quantidade de itens
print(len(dic_produtos))

# retirar um item do dicionario