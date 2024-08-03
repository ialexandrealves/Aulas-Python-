faturamento = 1000 
custo = 700 
lucro = faturamento - custo

print (" faturamento foi de {}, custo foi de {}, Lucro foi de {} ".format(faturamento, custo, lucro))

meu_email = "alexandre@gmail.com"

# maiúscula
meu_email = meu_email.upper()
print (meu_email)

# minúscula
meu_email = meu_email.lower()
print (meu_email)


# "@"
print(meu_email.find("@")) # -1 quando não encontrar

# tamanho do texto
print(len(meu_email))

# pegar um caracter
print(meu_email[2])

print(meu_email[2])

# pegar um pedaço do texto

print(meu_email[:3])
print(meu_email[1:3])

# trocar um pedaço do texto

novo_email = meu_email.replace("gmail.com", "hotmail.com")
print(novo_email)


#trabalhar com nomes
nome = "alexandre alves"

print(nome.capitalize())
print(nome.title())

# pegar o servidor do email
posicao_arroba = meu_email.find("@") +1
servidor = meu_email[posicao_arroba:]
print(servidor)

# pegar o primeiro nome

posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]
print(primeiro_nome.capitalize())


# pegar o sobrenome

sobrenome = nome[posicao_espaco +1:]
print(sobrenome.capitalize())

# casos especiais - formatações númericas em texto
print (f" faturamento foi de R${faturamento:.2f}, custo foi de R${custo:.2f}, Lucro foi de R${lucro:.2f}")