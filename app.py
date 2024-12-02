from flask import Flask, g
from flask_cors import CORS
import mysql.connector
from login.login import login_bp
from chamados.add_chamados import add_chamado_bp
from chamados.list_user_chamados import list_user_chamados_bp
from chamados.list_chamados import list_chamados_bp
from colaboradores.list_colaboradores import list_colaboradores_bp
from chamados.edit_chamado import edit_chamado_bp
from artigos.list_artigos import list_artigos_bp
from artigos.add_artigos import add_artigos_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(login_bp)
app.register_blueprint(add_chamado_bp)
app.register_blueprint(list_user_chamados_bp)
app.register_blueprint(list_chamados_bp)
app.register_blueprint(list_colaboradores_bp)
app.register_blueprint(edit_chamado_bp)
app.register_blueprint(list_artigos_bp)
app.register_blueprint(add_artigos_bp)


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)