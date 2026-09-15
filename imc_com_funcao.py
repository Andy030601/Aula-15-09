def imc(peso, altura):
    resultado = (peso/altura**2)
    
    if resultado <18.5:
        print(f'Seu IMC é {resultado:.1f}, você está abaixo do peso.')
    elif resultado <25:
        print(f'Seu IMC é {resultado:.1f}, você está no peso ideal.')
    elif resultado <30:
        print(f'Seu IMC é {resultado:.1f}, você está com sobrepeso.')
    else:
        print(f'Seu IMC é {resultado:.1f}, você está obeso.')
    

kg = float(input('Qual seu peso atual? '))
alt = float(input('Qual sua altura? '))

imc(kg, alt)
