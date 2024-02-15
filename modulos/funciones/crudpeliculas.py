import os 
import json 

def savejson(pelicula):
    with open('peliculas.json', 'w') as json_file:
        json.dump(pelicula, json_file, indent=4)

def agregarPelicula(paux = None):
    with open('peliculas.json', 'r') as json_file:
        pelicula = json.load(json_file)
            
    with open('generos.json', 'r') as json_file:
        generos = json.load(json_file)
        
    with open('actores.json', 'r') as json_file:
        actores = json.load(json_file)
    
    with open('formatos.json', 'r') as json_file:
        formatos = json.load(json_file)
        
    auxg = []        
    def asignarGeneros():
        os.system('cls')
        for i, value in enumerate(generos):
            for i1,valu in value.items():
                print("-----------------------")
                print(f'Id: {valu["id"]} \nNombre: {valu["nombre"]}')    
            print("-----------------------")
        gen = input("Ingrese el id del genero al que pertenece la pelicula: ").upper()
        for i, value in enumerate(generos):
            for i1,valu in value.items():
                if gen == valu["id"]:
                    infg = value
                    auxg.append(infg)
        s = input("Desea agregar otro genero a la pelicula?(S/N): ").upper()
        if s == "S":
            asignarGeneros()
        return auxg
    auxa = []
    def asignarActor():
        os.system('cls')
        for i, value in enumerate(actores):
            for i1,valu in value.items():
                print("-----------------------")
                print(f'Id: {valu["id"]} \nNombre: {valu["nombre"]}')    
            print("-----------------------")
        gen = input("Ingrese el id del actor al que pertenece la pelicula: ").upper()
        for i, value in enumerate(actores):
            for i1,valu in value.items():
                if gen == valu["id"]:
                    valu["rol"] = input("Ingrese el rol que cumple el actor en la pelicula(Protagonista/Antagonista/Reparto): ").upper()
                    infa = value
                    auxa.append(infa)
        s = input("Desea agregar otro actor a la pelicula?(S/N): ").upper()
        if s == "S":
            asignarActor()
        return auxa
    auxf = []
    def asignarFormato():
        os.system('cls')
        for i, value in enumerate(formatos):
            for i1,valu in value.items():
                print("-----------------------")
                print(f'Id: {valu["id"]} \nFormato: {valu["nombre"]}')    
            print("-----------------------")
        gen = input("Ingrese el id del formato de la pelicula: ").upper()
        for i, value in enumerate(formatos):
            for i1,valu in value.items():
                if gen == valu["id"]:
                    valu["nroCopias"] = int(input("Ingrese el numero de copias de la pelicula: "))
                    valu["valorPrestamo"] = int(input("Ingrese el valor del prestamo de la pelicula: "))
                    inff = value
                    auxf.append(inff)
        s = input("Desea agregar otro formato a la pelicula?(S/N): ").upper()
        if s == "S":
            asignarFormato()
        return auxf
        
    if paux == None:
        id = str(len(pelicula) + 1)
        id = ("P"+id)
        inf = {
            id : {
                "id" : id,
                "nombre": input("Ingrese el nombre de la pelicula a registrar: ").upper(),
                "duracion" :input("Ingrese la duracion de la pelicula(HH/MM): "),
                "sinopsis" : input("Ingrese la sinopsis de la pelicula: "),
                "generos" : asignarGeneros(),
                "actores" : asignarActor(),
                "formato" : asignarFormato()
            }
        }
        pelicula.append(inf)
        savejson(pelicula)
        print("La pelicula fue creada")
        os.system('pause')
    else:
        inf = {
            paux : {
                "id" : paux,
                "nombre": input("Ingrese el nombre de la pelicula a registrar: ").upper(),
                "duracion" :input("Ingrese la duracion de la pelicula(HH/MM): "),
                "sinopsis" : input("Ingrese la sinopsis de la pelicula: "),
                "generos" : asignarGeneros(),
                "actores" : asignarActor(),
                "formato" : asignarFormato()
            }
        }
        return inf

def actualizarPelicula():
    
    with open('peliculas.json', 'r') as json_file:
        pelicula = json.load(json_file)
    
    id = input("Ingrese el id de la pelicula a actualizar: ").upper()
    for i, value in enumerate(pelicula):
        for i2,val in value.items():
            if id == val["id"]:
                pelicula[i] = agregarPelicula(id)
                savejson(pelicula)
                print("La pelicula se ha actualizado")
                os.system('pause')
                return
    print("No hay ninguna pelicula con ese id")
    os.system('pause')
    return

