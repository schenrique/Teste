#Faça um algoritmo que leia o preço de um produto e seu novo preço com 5% de desconto
preco = float(input('Digite o preço do produto: '))
descon = (preco /100) *5
precoprom = preco-descon
print('O novo preço com desconto de 5% é de {}'.format(precoprom))