# Taller 1 Ejercicio practico -calculadora
# Jasmel Blanco Maldonado
# 25/05/2024

print("")
print ('Escriba los numeros y el simbolo de la operacion que desea realizar ( + , - , * , / )')
print("")

numero1 = float (input('Ingrese el primer numero: '))
operacion = str(input ('Ingrese la operacion:'))
numero2 = float (input('Ingrese el segundo numero: '))


if operacion == str ('+') :
    print ("")
    print ('la operación de:',numero1,'+',numero2,'=',numero1+numero2)
elif operacion == str ('-'):
    print ("")
    print ('la operación de:',numero1,'-',numero2,'=',numero1-numero2)
elif operacion == str ('*'):
    print ("")
    print ('la operación de:',numero1,'x',numero2,'=',numero1*numero2)
elif operacion == str ('/'):
    print ("")
    print ('la operación de:',numero1,'/',numero2,'=',("{0:.2f}".format(numero1/numero2)))
else : 
    print('No es posible realizar la operación')
    print("")