from flask import Blueprint, jsonify, request
from models.models import Producto
import db

productos_api = Blueprint('productos_api', __name__)

@productos_api.route('/', methods=['GET'])
def api_get_productos():
    productos = Producto.query.all()
    return jsonify([producto.as_dict() for producto in productos])

@productos_api.route('/<int:id>', methods=['GET'])
def api_get_producto(id):
    producto = Producto.query.get(id)
    if producto:
        return jsonify(producto.as_dict())
    return jsonify({'error': 'Producto no encontrado'}), 404
