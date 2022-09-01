
def ejercicio1():

    archivo=open("Microdato_Censo2017-Hogares.csv")
    total=0
    for x in archivo:
        x=x.strip()             #Borra los caracteres especiales a la derecha de la linea
        x=x.split(";")          #Split borra los caracteres que esten dentro de ()
        if x[0]=="9":             #0 en la lista es la region y 9 el tipo de hogar
            if x[9]=="4":         #SI el tipo de hogar es el Nuclear biparental (4) en la lista de hogar tipo
                total +=1       #Lo mismo que total=total+1
    print("El total de hogares en la 9na region de tipo compuesto es: ",total)

ejercicio1()