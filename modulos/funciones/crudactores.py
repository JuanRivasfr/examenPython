import os 
import json 

def savejson(actores):
    with open('actores.json', 'w') as json_file:
        json.dump(actores, json_file, indent=4)
#Crear generos
def crearActor():
    with open('actores.json', 'r') as json_file:
        actores = json.load(json_file)
    
    
    id = str(len(actores) + 1)
    id = ("A"+id)
    inf = {
        id : {
            "id" : id,
            "nombre": input("Ingrese el nombre del actor a registrar: ").upper()
        }
    }
    
    for i, value in enumerate(actores):
        for i1, valu in value.items():
            if inf[id]["nombre"] == actores[i][i1]["nombre"]:
                print("El actor ya esta registrado")
                os.system('pause')
                return
    
    actores.append(inf)
    savejson(actores)
#Listar generos
def listarActores():
    with open('actores.json', 'r') as json_file:
        actores = json.load(json_file)
    
    for i, value in enumerate(actores):
        for i1,valu in value.items():
            print("-----------------------")
            print(f'Id: {valu["id"]} \nNombre: {valu["nombre"]}')    
        print("-----------------------")
    os.system('pause')

def eliminarActor():
    with open('actores.json', 'r') as json_file:
        actores = json.load(json_file)
        
    id = input("Ingrese el id del actor a eliminar: ").upper()
    for i, value in enumerate(actores):
        for i2, val in value.items():
            if id == val["id"]:
                actores.pop(i)
                savejson(actores)
                print("Se ha eliminado el actor")
                os.system('pause')