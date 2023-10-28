#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
precokm=0.15
precodia=60
kmrodados=float(input('Quantos km foram percorridos pelo carro: '))
dias=int(input('Dias alugados: '))
valordia=dias*precodia
valorkm=kmrodados*precokm
valortotal=valordia+valorkm
print('O valor de {}km é de {:.2f}\nO valor de {} dias alugados é de {} reais\nTotal do aluguel: {:.2f }'.format(kmrodados,valorkm,dias,valordia,valortotal))