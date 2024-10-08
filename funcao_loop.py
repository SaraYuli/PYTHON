#função - bloco chando linha ---

def linha():
    print('-'*55)

# LOOP FOR (LISTA)

linha()
nome = ['Jesus, Sara, Davi, Helena']

for nome in nome:
  print('Nomes que eu acho bonito: {}'.format(nome))

linha()

#LOOP FOR (NUMERO)

for i in range(5):
    print(i)

linha()

#lOOP WHILER ()

x = 10

while x > 0:
    print('Contagem regressiva: {}'.format(x))
    x -=1

print('FELIZ ANO NOVO!!!')
