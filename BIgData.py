
def ejercicio1():

    archivo=open("Microdato_Censo2017-Hogares.csv")
    total=0
    for x in archivo:
        x=x.strip()             #Borra los caracteres especiales a la derecha de la linea
        x=x.split(";")          #Split borra los caracteres que esten dentro de ()
        if x[0]=="9":           #0 en la lista es la region y 9 el tipo de hogar, define el filtro de la region por numero
            if x[9]=="4":       #SI el tipo de hogar es el Nuclear biparental (4) en la lista de hogar tipo, define el tipo de hogar
                total +=1       #Lo mismo que total=total+1
    print("El total de hogares en la 9na region de tipo compuesto es: ",total)

ejercicio1()


============================================================

Diccionario

total=0
comunas={} #Diccionario vacio
for linea in archivo:
    linea = linea.rstrip()
    linea = linea.split(";")
    if linea[0] == "9": # Define el filtro de la region por numero, el que esta entre comillas define el buscador de comunas
        if linea[9] == "4":
            comunas[linea[2]]=comunas.get(linea[2],0)+1
#print(comunas)
# despliegue de los valores resultantes de la busqueda por comuna
for c,v in comunas.items():
    print("Comuna: ",c, "Total: ",v)
