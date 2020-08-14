#Exercício 1 - antecessor e sucessor de um número
n1 = int(input('Digite um número: '))
print('o número antecessor a este é {:=^3}, e o sucessor é {:=^3}!'.format(n1 - 1, n1 + 1))
print()

#Exercício 2 - algorítimo que leia um número e mostre o seu dobro e sua raiz quadrada
print('Seu dobro é {}, e sua raiz quadrada é {:.3f}'.format(n1 * 2, n1 ** (1/2)))
print()

#Exercício 3 - programa que leia duas notas e gere uma média
p1 = float(input('Nota prova 1: '))
p2 = float(input('Nota prova 2: '))
print('A média é: {}'.format((p1 + p2)/2))
print()

#Exercício 4 - programa que converte metros para centímetros e milímetros
m1 = float(input('Quantos metros: '))
print('Centímetros: {} cm \nMilímetros: {} mm'.format(m1 * 100, m1 * 1000))
print()

#Exercício 5 - ler número inteiro qualquer e mostrar sua tabuada
e1 = int(input('Digite um número inteiro: '))
print('Tabuada de {}'.format(e1))
print('Por 1: {} \nPor 2: {} \nPor 3: {} '
      '\nPor 4: {} \nPor 5: {} \nPor 6: {} '
      '\nPor 7: {} \nPor 8: {} \nPor 9: {} '
      '\nPor 10: {}'.format(e1 * 1, e1 * 2,
                            e1 * 3, e1 * 4,
                            e1 * 5, e1 * 6,
                            e1 * 7, e1 * 8,
                            e1 * 9, e1 * 10,))
print()

#Exercício 6 - conversor de moedas
moeda = float(input('Reais: '))
print('Dólar: {:.2f} \nEuros: {:.2f} \nLibras: {:.2f}'.format(moeda * 5.3, moeda * 6.0, moeda * 7.02))
print()

#Exercício 7 - ler a largura e altura de uma parede para
# calcular área e quantos litros de tinta (2m2)
l1 = float(input('Qual a largura da parede? '))
a1 = float(input('Qual a altura da parede? '))
print('Área: {} \nQuantidade de tinta: {} litros'.format(l1 * a1, (l1 * a1) / 2))
print()


#Exercício 8 - ler o preço de um produto e mostrar novo preço, com 5% de desconto
preço = float(input('Preço: R$ '))
print('Novo preço: R$ {}'.format(preço * 0.95))
print()

#Exercício 9 - ler o salário de um funcionário e mostre o novo valor com 15% de aumento
s1 = float(input('Salário: R$ '))
print('Novo salário: R$ {:.2f}'.format(s1 * 1.15))
print()