from datetime import datetime
minuto = datetime.now().minute
if int(minuto)%2==0:
    print("O minuto atual é par")
else:
    print("O minuto atual é ímpar")