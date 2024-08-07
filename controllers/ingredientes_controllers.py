from flask import Blueprint, jsonify
from models.models import Ingrediente
import db

ingredientes_bp = Blueprint('ingredientes', __name__)

@ingredientes_bp.route('/', methods=['GET'])
def get_ingredientes():
    ingredientes = Ingrediente.query.all()
    return jsonify([ingrediente.as_dict() for ingrediente in ingredientes])

@ingredientes_bp.route('/<int:id>', methods=['GET'])
def get_ingrediente(id):
    ingrediente = Ingrediente.query.get(id)
    if ingrediente:
        return jsonify(ingrediente.as_dict())
    return jsonify({'error': 'Ingrediente no encontrado'}), 404
