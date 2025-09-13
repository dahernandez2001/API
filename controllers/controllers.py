from flask import Blueprint, request, jsonify
from services.service import pelicula
pelicula_bp = Blueprint("pelicula_bp, __name__")

#Importar la sesión de la base de datos
from config.config import get_db_session

#Instancia globar de servicio
service = pelicula (get_db_session)

pelicula_bp = Blueprint("pelicula_bp, __name__")

#READ (R): Leer todos los pelicula
#Método: GET Obtener (solicita datos al servidor ) 

@pelicula_bp.route("pelicula", methods=["GET"])
def get_pelicula():

    pEñicula= service.listar_pelicula()
    return jsonify([{"id": l.id, "name": l.name} for l in pelicula]), 200 #JsoniFy convierte el diccionario de pelicula en una respuesta JSON

#Obtener pelicula por ID 

@pelicula_bp.route("/pelicula/<int:id>", methods=["GET"]) #Variable dinámica que indica que la parte <...> es una variable
def obtener_pelicula_por_ID(pelicula_id):

    pelicula = service.obtener_pelicula(pelicula_id)
    if pelicula:
        return jsonify({"id": pelicula.id, "name": pelicula.name}), 200 
    return jsonify({"error": "pelicula no encontrado"}), 404 

#CREATE (C): Crear un nuevo pelicula
#Método: POST para crear un nuevo pelicula

@pelicula_bp.route("\pelicula", methods=["POST"])
def create_pelicula():
    
    data=request.get_json()
    name=data.get("name")
    if not name:
        return jsonify({"error": "El nombre es obligatorio"}), 400 
    band = service.crear_banda(name)
    return jsonify({"id": band.id, "name": band.name}), 201 

#Update (U): Actualizar un pelicula
#Método: PUT actualizar pelicula con obtener el nuevo pelicula creado

@pelicula_bp.route("/pelicula/<int:id>", methods=["PUT"])
def actualizar_pelicula(pelicula_id):

    data=request.get_json()
    name=data.get("name")
    pelicula=service.actualizar_pelicula(pelicula_id, name)

    if pelicula:
        return jsonify({"id": pelicula_id, "name": pelicula.name}), 200
    return jsonify({"error": "pelicula no encontrado"}), 404

#Delete (D): Borrar un pelicula
#Método: DELETE para eliminar algún pelicula igualmente por ID

@pelicula_bp.route("/pelicula/<int:id>", methods=["DELETE"])
def eliminar_pelicula(pelicula_id):
    
    pelicula = service,eliminar_pelicula(pelicula_id)
    if pelicula:
        return jsonify({"message": "pelicula eliminado"}), 200
    return jsonify({"error": "pelicula no encontrado"}), 404