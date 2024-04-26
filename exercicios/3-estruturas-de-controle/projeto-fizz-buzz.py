# Criaremos um programa para substituir números por palavras em uma lista
#Divisivel por 3 - Substitua por 'Fizz'
#Divisivel por 5 - Substitua por 'Buzz'
#Divisivel por 3 e 5 - Substitua por 'FizzBuzz'

lista_numerica = list(range(15,31))
indice = 0

for numero in lista_numerica:
  if numero % 3 == 0 and numero % 5 == 0:
    lista_numerica[indice] = 'FizzBuzz'
  elif numero % 3 == 0:
    lista_numerica[indice] = 'Fizz'
  elif numero % 5 == 0:
    lista_numerica[indice] = 'Buzz'
  else:
    lista_numerica[indice] = numero
    indice += 1

    print(lista_numerica)
# 1. Crie uma lista com 15 números
# 2. Crie um for loop para percorrer todos os elementos da lista
# 3. Crie uma estrutura condicional para verificar cada número da lista:
# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"

