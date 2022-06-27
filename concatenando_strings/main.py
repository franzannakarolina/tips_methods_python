nome = 'Python'
hobby = 'programar'

# 1 - CONCATENAÇÃO SIMPLES USANDO +
s = 'Meu nome é ' + nome + ' e meu hobby é ' + hobby
print(s)

#  - CONCATENAÇÃO USANDO FSTRING
s = f'Meu nome é {nome} e meu hobby é {hobby}'
print(s)

# 3 - CONCATENAÇÃO USANDO FORMAT
s = 'Meu nome é {} e meu hobby é {}.format(nome, hobby)'
print(s)
