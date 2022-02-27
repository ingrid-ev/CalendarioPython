from calendar import month
from datetime import datetime

mes_atual = datetime.today().month

for mes in range(1, 13):
    # temporario
    if mes == mes_atual:
        if mes < 7:
            if mes % 2:
                # impar
                dias = 31
            else:
                #par
                dias = 30
        else:
            if mes % 2:
                # impar
                dias = 30
            else:
                #par
                dias = 31
for dia in range(1, dias + 1):
    print(f'{dia:>2}', end=' ')
    if not dia % 7 and dia > 1:
        print('\n')

