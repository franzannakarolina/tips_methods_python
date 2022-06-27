# append = adiciona um novo elemento no final da lista
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
livros.append('Android')
print(livros)

# insert = Insere um novo elemento na posição desejada
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
livros.insert(0, 'Oracle')
print(livros)

# pop = remove o ultimo elemento da lista
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
livros.pop()
print(livros)

# remove = remove um elemento da lista a partir do seu valor
print(livros)
livros.remove('Java')
print(livros)

# count = retorna o numero de ocorrencias de um elemento da lista
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
livros.count('Python')
print(livros)

# reverse = inverte as posições dos elementos da lista
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
livros.reverse()
print(livros)

# sort = ordena a lista numericamente ou alfabeticamente
livros = ['Java', 'SqlServer', 'Delphi', 'Python']
livros.sort()
print(livros)
