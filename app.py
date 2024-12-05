from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
import mysql.connector
from login.login import login_bp
from chamados.add_chamados import create_add_chamado_blueprint
from chamados.list_user_chamados import list_user_chamados_bp
from chamados.list_chamados import list_chamados_bp
from colaboradores.list_colaboradores import list_colaboradores_bp
from chamados.edit_chamado import edit_chamado_bp
from artigos.list_artigos import list_artigos_bp
from artigos.add_artigos import add_artigos_bp

app = Flask(__name__)
CORS(app)  # Certifique-se de que o CORS esteja configurado para permitir conexões de seu frontend.

socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')  # async_mode='eventlet' é necessário para suporte a WebSockets

app.register_blueprint(login_bp)
app.register_blueprint(create_add_chamado_blueprint(socketio)) 
app.register_blueprint(list_user_chamados_bp)
app.register_blueprint(list_chamados_bp)
app.register_blueprint(list_colaboradores_bp)
app.register_blueprint(edit_chamado_bp)
app.register_blueprint(list_artigos_bp)
app.register_blueprint(add_artigos_bp)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
