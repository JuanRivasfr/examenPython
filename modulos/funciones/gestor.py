import os
import json

def listarporgenero():
    with open('peliculas.json', 'r') as json_file:
        pelicula = json.load(json_file)
    
    gen = input("Digite el genero de peliculas que desea consultar: ").upper()
    for i, value in enumerate(pelicula):
        for i1, value1 in value.items():
            for i23, value23 in value1.items():
                if i23 == "generos":
                    for i2, value2 in enumerate(value23):
                        for i3, value3 in value2.items():
                            if value3["nombre"] == gen:
                                print("-----------------")
                                print(f'ID: {value1["id"]} \nNombre: {value1["nombre"]} \nDuracion: {value1["duracion"]} \nSinopsis {value1["sinopsis"]}')
                                print("-----------------")
    os.system('pause')
    
def listarsilvestre():
    with open('peliculas.json', 'r') as json_file:
        pelicula = json.load(json_file)
    
    for i, value in enumerate(pelicula):
        for i1, value1 in value.items():
            for i23, value23 in value1.items():
                if i23 == "actores":
                    for i2, value2 in enumerate(value23):
                        for i3, value3 in value2.items():
                            if value3["nombre"] == "SILVESTER STALLONE" and value3["rol"] == "PROTAGONISTA":
                                print("-----------------")
                                print(f'ID: {value1["id"]} \nNombre: {value1["nombre"]} \nDuracion: {value1["duracion"]} \nSinopsis {value1["sinopsis"]}')
                                print("-----------------")
    os.system('pause')
    
def bymostrar():
    
    with open('peliculas.json', 'r') as json_file:
        pelicula = json.load(json_file)
    
    id = input("Digite el id de la pelicula que desea consultar: ").upper()
    for i, value in enumerate(pelicula):
        for i1, value1 in value.items():
            if id == value1["id"]:
                print("-----------------")
                print(f'ID: {value1["id"]} \nNombre: {value1["nombre"]} \nDuracion: {value1["duracion"]} \nSinopsis {value1["sinopsis"]}')
                for i23, value23 in value1.items():
                    if i23 == "actores":
                        for i2, value2 in enumerate(value23):
                            for i3, value3 in value2.items():
                                print("-----------------")
                                print(f'Actores: {value3["nombre"]}')
                                print("-----------------")
    os.system('pause')
