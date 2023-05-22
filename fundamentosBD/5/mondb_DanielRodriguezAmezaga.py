import pymongo
from datetime import datetime

client = client = pymongo.MongoClient("localhost",27017)
# Conexión
db = client.actividad

# Insertar datos
print("\nInsertamos los datos...")
db.notas.insert_one({'nombre': 'Pedro López', 'edad': 25, 
                     'email': 'pedro@eip.com', 'notas': 5.2, 
                     'fecha': datetime.now()})

db.notas.insert_one({'nombre': 'Julia García', 'edad': 22, 
                     'email': 'julia@eip.com', 'nota': 7.3,
                     'fecha': datetime.now()})
                    
db.notas.insert_one({'nombre': 'Amparo Mayoral', 'edad': 28, 
                     'email': 'amparo@eip.com', 'nota': 8.4, 
                     'fecha': datetime.now()})
                    
db.notas.insert_one({'nombre': 'Juan Martínez', 'edad': 30, 
                     'email': 'juan@eip.com', 'nota': 6.8,
                     'fecha': datetime.now()})

# Visualizar todos los datos hasta ahora
col = db.notas
print("\nDatos Insertados:")
for docum in col.find({}):
    print(docum)
    
    
# Actualizar datos con "update_one"
print("\nActualizamos las notas de Amparo y Juan...")
col.update_one({
    "nombre": "Amparo Mayoral"
}, {
    "$set": {
        "nota": 9.3
    }
})

col.update_one({
    "nombre": "Juan Martínez"
}, {
    "$set": {
        "nota": 7.2
    }
})

# Visualizar todos los datos hasta ahora
col = db.notas
print("\nMostramos los datos de nuevo:")
for docum in col.find({}):
    print(docum)


# Buscar notas mayores que 7 y menores que 7.5
col = db.notas
print("\nMostrar notas entre 7 y 7.5:")
for docum in col.find({
    "nota": {
        # Usamos $gt para decir "mayor que"
        "$gt": 7
    },
        "nota": {
        # Usamos $lt para decir "menor que"
        "$lt": 7.5
    }
}):
    print(docum)

# Encontar un dato
# doc = col.find_one({
#     "nombre": "Amparo Mayoral"
# })
# print("Buscando un elemenro por su nombre:(Amparo Mayoral)")
# print(doc)

# Eliminar uno "delete_one" o muchos "delete_many"
print("\nEliminando a Pedro...")
col.delete_one({
    "nombre": "Pedro López"
})

# Visualizar todos los datos hasta ahora(Pedro Eliminado)
col = db.notas
print("\nDatos finales:")
for docum in col.find({}):
    print(docum)
    
