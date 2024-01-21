from pymongo import MongoClient
from datetime import datetime

def main():
    host = "localhost"
    port = 27017
    name = "mi_mongo"
    coleccion_nombre = "personas"
    
    client = MongoClient(host, port)
    db = client[name]
    
    coleccion = db[coleccion_nombre]
    
    personas_data = [
        {
            "dni": "123456789",
            "nombre": "Juan",
            "apellidos": "Pérez",
            "fecha_nacimiento": datetime(1990, 5, 15),
            "correo": "juan.perez@example.com",
            "telefono": "1234567890",
        },
        {
            "dni": "987654321",
            "nombre": "María",
            "apellidos": "Gómez",
            "fecha_nacimiento": datetime(1985, 8, 25),
            "correo": "maria.gomez@example.com",
            "telefono": "9876543210",
        },
        {
            "dni": "555555555",
            "nombre": "Carlos",
            "apellidos": "López",
            "fecha_nacimiento": datetime(1995, 3, 10),
            "correo": "carlos.lopez@example.com",
            "telefono": "5555555555",
        },
    ]
        
    coleccion.insert_many(personas_data)

    # Consultar los datos para verificar que se han insertado correctamente
    result = coleccion.find()

    # Mostrar los datos del primer elemento de la coleccion
    first_document = coleccion.find_one()
    print("Primer documento de la colección:")
    print(first_document)
    
    # Mostrar solo algunos campos específicos
    second_document_projection = {"nombre": 1, "apellidos": 1, "fecha_nacimiento": 1}
    second_document = coleccion.find_one({}, second_document_projection)
    print("\nCampos específicos seleccionados:")
    print(second_document)
    
    # Actualizar el tercer documento
    dni_tercero = {"dni": "555555555"}
    telefono_nuevo = "937610053"
    update = {"$set": {"telefono": telefono_nuevo}}
    coleccion.update_one(dni_tercero, update)
    
    # Mostrar el tercer documento después de la actualización
    tercero_nuevo = coleccion.find_one(dni_tercero)
    print("\nTercer documento después de la actualización:")
    print(tercero_nuevo)
    
    # Cerrar la conexión
    client.close()
        
main()