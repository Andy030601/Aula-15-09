numeros = []

quantidade_number = int(input( 'Quantos números você deseja verificar: '))

for i in range(quantidade_number):
    num = int(input(f'Digite o {i+1}° número: '))
    numeros.append(num)
 
def contar_pares(lista):
    contador = 0
    for num in lista:
        if num % 2 == 0:
            contador += 1
    print(f'A quantidade de números pares é de: {contador} ')
        
contar_pares(numeros)
