from flask import Blueprint, jsonify, request
from models.models import Producto
import db

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    return jsonify([producto.as_dict() for producto in productos])

@productos_bp.route('/<int:id>', methods=['GET'])
def get_producto(id):
    producto = Producto.query.get(id)
    if producto:
        return jsonify(producto.as_dict())
    return jsonify({'error': 'Producto no encontrado'}), 404
