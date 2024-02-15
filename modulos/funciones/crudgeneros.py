import os 
import json 

def savejson(generos):
    with open('generos.json', 'w') as json_file:
        json.dump(generos, json_file, indent=4)
#Crear generos
def crearGenero():
    with open('generos.json', 'r') as json_file:
        generos = json.load(json_file)
    
    
    id = str(len(generos) + 1)
    id = ("G"+id)
    inf = {
        id : {
            "id" : id,
            "nombre": input("Ingrese el nombre del genero a registrar: ").upper()
        }
    }
    
    for i, value in enumerate(generos):
        for i1, valu in value.items():
            if inf[id]["nombre"] == generos[i][i1]["nombre"]:
                print("El genero ya esta registrado")
                os.system('pause')
                return
    
    generos.append(inf)
    savejson(generos)
#Listar generos
def listarGenero():
    with open('generos.json', 'r') as json_file:
        generos = json.load(json_file)
    
    for i, value in enumerate(generos):
        for i1,valu in value.items():
            print("-----------------------")
            print(f'Id: {valu["id"]} \nNombre: {valu["nombre"]}')    
        print("-----------------------")
    os.system('pause')