#condiciones

from operator import length_hint
from tabnanny import verbose


esMayorEdad =True
#if not esMayorEdad  and or
if esMayorEdad == True:
   print('es mayor de edad')
   print('esto es del if')
else:
    print('no es mayor de edad')
    print('esto es parte del elfe')

print('mensaje de prueba')#recordar tabulacion

personas=[
    {
    'nombre':  "Shayd",
    'apellido': "Ruano",
    'edad': 18,
    'materias': ["Base de datos II", "Lenguaje de cuarta generacion"],
    },
    {
    'nombre':  "Laura",
    'apellido': "Erazo",
    'edad': 16,
    'materias': ["Base de datos I", "Lenguaje orientado a objectos"],
    },
    {
    'nombre':  "Carla",
    'apellido': "Torres",
    'edad': 20,
    'materias': ["Lenguaje Orientado a Eventos"],
    }
]
'''
for per in personas:
    print(per)
'''
for per in personas:
    print(per['nombre'])

nombrepersona='roberto'
print(nombrepersona[2])#imprime b
# + para concatenar
'''verbos regulares ar  er ir
solicitr verbo en infinitivo
tomar ese everbo y conjugarlo en en personas 

verbos= 'morir'

lfinal=verbos[len(verbos)-1]
print(lfinal)
#afinal=verbos[len(verbos-1)]'''

personas[
     'ellos':{
         'ar':'an',
     }
]

verbo=input()
terminacion=verbo[len(verbo)-2]+ verbo[len(verbo)-1]
verbosinterminacion=verbo.replace(terminacion,'')

for persona in personas:
   print(persona)
   print(verbosinterminacion)
   print(personas[persona][terminacion])
   print(persona,verbosinterminacion+personas[persona][terminacion])
# prueba



















