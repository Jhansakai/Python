#reto promedio notas estudiantes
#Jasmel Blanco Maldonado
#25/05/2024
print ("")
print ("""Estas son las notas que tiene los tres mejores estudiantes en las diferentes materias
      • Español
      • Ingles
      • Matematicas
      • Sociales
      • Biologia
       """)

print ('Ingresa las notas que saco Maria:')
print ("")

notas_Maria = []
while True:
      nuevo_notaM = input ('Ingresa la nota: ')
      if nuevo_notaM.isnumeric():
            nuevo_notaM = int (nuevo_notaM)

      notas_Maria.append(nuevo_notaM)
      if nuevo_notaM == ("") :
        break    
notas_Maria.pop(-1)
totalM = sum (notas_Maria)
promedioM = (totalM / (len (notas_Maria)))
print ("")

print ('Ingresa las notas que saco Daniel:')
notas_Daniel = [ ]
print ("")
while True:
      nuevo_notaD = input ('Ingresa la nota: ')
      if nuevo_notaD.isnumeric():
            nuevo_notaD = int (nuevo_notaD)

      notas_Daniel.append(nuevo_notaD)
      if nuevo_notaD == (""):
        break   
notas_Daniel.pop(-1)   
totalD = sum (notas_Daniel)          
promedioD = (totalD / (len (notas_Daniel)))
print ("")

print ('Ingresa las notas que saco Carlos:')
print ("")
notas_Carlos =[]
while True:
      nuevo_notaC = input ('Ingresa la nota: ')
      if nuevo_notaC.isnumeric():
            nuevo_notaC = int (nuevo_notaC)

      notas_Carlos.append(nuevo_notaC)
      if nuevo_notaC == ("") :
        break    
notas_Carlos.pop(-1)
totalC = sum (notas_Carlos)
promedioC = (totalC/ (len(notas_Carlos)))
print ("")

print ('las notas son las siguientes',)
print ("")
print ('Maria',notas_Maria)
print ("")
print ('Daniel',notas_Daniel)
print ("")
print ('Carlos',notas_Carlos)
print ("")

if promedioM > promedioD and promedioM > promedioC :
    print ('El mejor promedio lon tiene Maria con:',promedioM)
elif promedioD > promedioM and promedioD > promedioC :
    print ('El mejor promedio lo tiene Daniel con:',promedioD)
elif promedioM == promedioD :
    print ('Hay empate en el promedio de Maria y Daniel',promedioM)
elif promedioM == promedioC :
    print ('Hay empate en el promedio de Maria y Carlos',promedioM)
elif promedioC == promedioD : 
    print ('Hay empaque en el promedio de Carlos y Daniel',promedioC)
elif promedioM == promedioC and promedioM == promedioD :
    print ('Hay triple empate en el promedio de Maria, Darlos y Daniel',promedioM)        
    print('')
else  :
    print ('El mejor promedio lo tiene Carlos con:',promedioC)
print ("")