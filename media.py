def nota(n1,n2,n3):
    calculo = (n1 + n2 + n3)/3
    
    if calculo >=5:
        print(f'Sua média é igual a {calculo:.1f}, você está aprovado!!')
    else:
        print(f'Sua média é igual a {calculo:.1f}, você está na recuperação!!')
        
not1 = float(input('Qual a 1° nota? '))
not2 = float(input('Qual a 2° nota? '))
not3 = float(input('Qual a 3° nota? '))

nota(not1, not2, not3)
