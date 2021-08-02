#Exercício Treino 1 - Escreva uma função que recebe dois parâmetros (números) 
# e imprime o menor dos dois. Se eles forem iguais, imprima que são valores idênticos.

def imprime_menor(a, b):
  if a < b:
    print(a)
  elif a > b:
    print(b)
  else:
    print("Os números são iguais.")
imprime_menor(5,5)