from flask import Blueprint, jsonify, request
from models.models import Ingrediente
import db

ingredientes_api = Blueprint('ingredientes_api', __name__)

@ingredientes_api.route('/', methods=['GET'])
def api_get_ingredientes():
    ingredientes = Ingrediente.query.all()
    return jsonify([ingrediente.as_dict() for ingrediente in ingredientes])

@ingredientes_api.route('/<int:id>', methods=['GET'])
def api_get_ingrediente(id):
    ingrediente = Ingrediente.query.get(id)
    if ingrediente:
        return jsonify(ingrediente.as_dict())
    return jsonify({'error': 'Ingrediente no encontrado'}), 404
