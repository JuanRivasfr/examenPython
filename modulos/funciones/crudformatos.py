import os 
import json 

def savejson(formatos):
    with open('formatos.json', 'w') as json_file:
        json.dump(formatos, json_file, indent=4)
#Crear formatos
def crearFormato():
    with open('formatos.json', 'r') as json_file:
        formatos = json.load(json_file)
    
    
    id = str(len(formatos) + 1)
    id = ("F"+id)
    inf = {
        id : {
            "id" : id,
            "nombre": input("Ingrese el nombre del formato a registrar: ").upper()
        }
    }
    
    for i, value in enumerate(formatos):
        for i1, valu in value.items():
            if inf[id]["nombre"] == formatos[i][i1]["nombre"]:
                print("El formato ya esta registrado")
                os.system('pause')
                return
    
    formatos.append(inf)
    savejson(formatos)
#Listar formatos
def listarFormato():
    with open('formatos.json', 'r') as json_file:
        formatos = json.load(json_file)
    
    for i, value in enumerate(formatos):
        for i1,valu in value.items():
            print("-----------------------")
            print(f'Id: {valu["id"]} \nFormato: {valu["nombre"]}')    
        print("-----------------------")
    os.system('pause')