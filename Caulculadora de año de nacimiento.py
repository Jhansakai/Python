# Taller 1 Ejercicio practico -calcular año de nacimiento
# Jasmel Blanco Maldonado
# 25/05/2024

import datetime
print("")
año_actual = datetime.datetime.today().year
edad = int (input ('Ingresa tu edad o la edad que vas a tener este año :'))

año_nacimiento = año_actual - edad

print ('El año en que naciste es :',año_nacimiento)
print ("")