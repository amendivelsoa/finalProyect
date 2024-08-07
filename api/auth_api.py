from flask import Blueprint, jsonify, request
from models.models import Usuario
import db

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/login', methods=['POST'])
def api_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = Usuario.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify({'message': 'Login exitoso'}), 200
    return jsonify({'error': 'Usuario o contraseña incorrectos'}), 401
