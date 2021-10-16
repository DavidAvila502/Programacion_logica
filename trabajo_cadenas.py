#Programa 04 
#Programa que elimine las letras pares si son vocales

#Funcion que detecta vocales
def detectar_vocales(letra):

    letra2 = letra.lower()
    vocales = 'aáeéiíoóuú'
    detector = False
    exist = vocales.find(letra2)
    if(exist >=0):
        detector = True

    return detector

cadena ="""Habitantes de las cuatro regiones purépechas de Michoacán bloquearon cinco tramos de otras tantas carreteras federales
 (Cherán-Zamora, Pátzcuaro-Uruapan, Nahuatzen-Paracho, Morelia-Lázaro Cárdenas y Uruapan-Los Reyes) para exigir reformas legislativas que
  les garanticen su autodeterminación y presupuesto directo que los ayuntamientos manejan unilateralmente y nunca llegan a las tenencias ni
   a las encargaturas (sic) del orden; además que reconozcan el sistema de seguridad y de justicia comunal.""" 

cadena_procesada = ''

indicador =0#Indica la posicion del ultimo caracter que se agrego a cadena_procesada

#Inicia for saltando de 2 en dos 
for letra in range(2,len(cadena)+2,2):

    muestra = cadena[letra-1:letra] #Otenemos letra en posicion par

    cadena_procesada = cadena_procesada + cadena[indicador:letra-1] #agregamos toda la cadena que antecede a la muestra a una nueva variable

    muestra_analizada = detectar_vocales(muestra) #Obtenemos resultados de la deteccion de vocales

    if(muestra_analizada == True):#Comprobamos si es vocal
    
      cadena_procesada = cadena_procesada + '' #Caso verdadero eliminamos la letra y añadimos a la nueva variable

      indicador = letra #Agregamos la posicion de esta ultima muestra

    else:
        cadena_procesada = cadena_procesada + muestra #Añadimos la muestra a la nueva cadena
        indicador = letra # Actualizamos el indicador
    
print(cadena_procesada)#Imprimimos resultado en pantalla



