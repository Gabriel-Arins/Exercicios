#soma entre números
s1 = int(input('Digite um número: '))
s2 = int(input('Digite outro: '))
soma = s1 + s2
print('A soma entre {} e {} é {}!'.format(s1, s2, soma))

#dissecar uma variável
v1 = input('Digite algo: ')
print('Qual é a classe dessa variável: {} '.format(type(v1)))
print('É um número? {}'.format(v1.isnumeric()))
print('Só tem espaços? {}'.format(v1.isspace()))
print('É alfabético? {}'.format(v1.isalpha()))
print('É alfanumérico? {}'.format(v1.isalnum()))
print('Está em caixa alta? {}'.format(v1.isupper()))
print('Está em caixa baixa? {}'.format(v1.islower()))
print('Está capitalizada? {}'.format(v1.istitle()))

#v1 é um objeto



