hora_1 = input('Digite as horas de 00 a 23: ')
min_1 = input('Digite os minutos de 00 a 59: ')

if hora_1.isnumeric() and min_1.isnumeric:
    hora_1 = int(hora_1)
    min_1 = int(min_1)
    
if hora_1 <= 0 >= 11 and min_1 >= 00:
    print (f'Bom dia!, são {hora_1}:{min_1} da manhã')
    
elif hora_1 <= 12 >= 17  and min_1 >= 00: 
    print (f'Boa tarde!, são {hora_1}:{min_1} da tarde')
    
elif hora_1 <= 18 >= 23  and min_1 >= 00:
    print (f'Boa Noite!, são {hora_1}:{min_1} da noite')
    
else:
    print ('Horário incorreto')
    