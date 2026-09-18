def calcular_medias(lista):
    media_number = sum(lista)/len(lista)
    
    return media_number

numeros = []

quantidade_number = int(input('Quantos números você deseja cadastrar: '))

for i in range(quantidade_number):
    informar_number = int(input(f'Informe o {i+1}° número: '))
    
    numeros.append(informar_number)
    
resultado = calcular_medias(numeros)
print(f'A média dos números digitados é: {resultado:.1f}')
