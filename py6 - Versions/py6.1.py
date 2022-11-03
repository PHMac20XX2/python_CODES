hora_1 = input('Digite as horas de 00 a 23: ')

if hora_1.isnumeric():
    hora_1 = int(hora_1)
    
    if hora_1 < 0 or hora_1 > 23:
        print("a")
        
    else: 
        hora_1 <= 11
        print (f'Bom dia!, são {hora_1}')
    
elif hora_1 <= 17:
    print (f'Boa tarde!, são {hora_1}')
    
else:
    print (f"Boa noite!, são {hora_1}")
    