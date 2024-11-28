from flask import Blueprint, request, jsonify, current_app
from mysql.connector import Error
from db import get_connection, close_connection

login_bp = Blueprint('login', __name__)

@login_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    senha = data.get('senha')

    if not usuario or not senha:
        return jsonify({"message": "Usuário ou senha não fornecidos"}), 400

    conn = get_connection()
    if not conn:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500

    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM colaboradores WHERE usuario = %s AND senha = %s", (usuario, senha))
        colaborador = cursor.fetchone()

        if colaborador:
            return jsonify({"message": "Colaborador autenticado", "tipo": "colaborador", "nome": colaborador['nome']}), 200

        cursor.execute("""
            SELECT usuarios.id, usuarios.nome, setores.nome AS setor
            FROM usuarios
            JOIN setores ON usuarios.setor = setores.id
            WHERE usuarios.usuario = %s AND usuarios.senha = %s
        """, (usuario, senha))
        usuario_bd = cursor.fetchone()

        if usuario_bd:
            return jsonify({
                "message": "Usuário autenticado",
                "tipo": "usuario",
                "nome": usuario_bd['nome'],
                "setor": usuario_bd['setor'],
                "id": usuario_bd['id']
            }), 200

        return jsonify({"message": "Usuário ou senha incorretos"}), 401
    except Error as e:
        return jsonify({"message": f"Erro ao acessar o banco de dados: {str(e)}"}), 500
    finally:
        cursor.close()
        close_connection(conn)