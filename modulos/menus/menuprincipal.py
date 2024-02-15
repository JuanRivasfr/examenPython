import os

from ..funciones.crudgeneros import crearGenero,listarGenero
from ..funciones.crudactores import crearActor,listarActores, eliminarActor
from ..funciones.crudformatos import crearFormato,listarFormato
from ..funciones.crudpeliculas import agregarPelicula, actualizarPelicula,eliminarPelicula, verPelicula, verTPelicula

def menuPrincipal():
    try:
        while True:
            os.system('cls')
            opc = int(input("1.Administracion de generos \n2.Administracion de actores \n3.Administracion de formatos \n4.Gestor de informes \n5.Gestor de peliculas \n6.Salir \n:"))
            match(opc):
                case 1:
                    while True:
                        os.system('cls')
                        opcg = int(input("1.Crear generos \n2.Listar generos \n3.Volver \n:"))
                        match(opcg):
                            case 1:
                                crearGenero()
                            case 2:
                                listarGenero()
                            case 3:
                                break
                case 2:
                    while True:
                        os.system('cls')
                        opca = int(input("1.Crear actores \n2.Listar actores \n3.Volver \n:"))
                        match(opca):
                            case 1:
                                crearActor()
                            case 2:
                                listarActores()
                            case 3:
                                break
                case 3:
                    while True:
                        os.system('cls')
                        opca = int(input("1.Crear formatos \n2.Listar formatos \n3.Volver \n:"))
                        match(opca):
                            case 1:
                                crearFormato()
                            case 2:
                                listarFormato()
                            case 3:
                                break
                case 5:
                    while True:
                        os.system('cls')
                        opca = int(input("1.Agregar pelicula \n2.Actualizar pelicula \n3.Eliminar pelicula \n4.Eliminar actor \n5.Buscar pelicula \n6.Ver todas las peliculas \n7.Volver \n:"))
                        match(opca):
                            case 1:
                                agregarPelicula()
                            case 2:
                                actualizarPelicula()
                            case 3:
                                eliminarPelicula()
                            case 4:
                                eliminarActor()
                            case 5:
                                verPelicula()
                            case 6:
                                verTPelicula()
                            case 7:
                                break
                case 6:
                    break
    except ValueError:
        print("Ingrese una opcion valida")
        os.system('pause')