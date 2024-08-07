from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from controllers.auth_controllers import auth_bp
from controllers.productos_controllers import productos_bp
from controllers.ingredientes_controllers import ingredientes_bp
from api.auth_api import auth_api
from api.productos_api import productos_api
from api.ingredientes_api import ingredientes_api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{os.getenv("USER_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("HOST_DB")}/{os.getenv("SCHEMA_DB")}'
app.config["SECRET_KEY"] = 'mi_secreto'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(productos_bp, url_prefix='/productos')
app.register_blueprint(ingredientes_bp, url_prefix='/ingredientes')
app.register_blueprint(auth_api, url_prefix='/api/auth')
app.register_blueprint(productos_api, url_prefix='/api/productos')
app.register_blueprint(ingredientes_api, url_prefix='/api/ingredientes')

from models.models import Usuario

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.errorhandler(403)
def forbidden(error):
    return render_template('error.html', message="No autorizado"), 403

if __name__ == '__main__':
    app.run(debug=True)
