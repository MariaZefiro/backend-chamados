from flask import Blueprint, jsonify
from db import get_connection, close_connection

list_user_chamados_bp = Blueprint('list_user_chamados', __name__)

@list_user_chamados_bp.route('/api/list_user_chamados/<int:user_id>', methods=['GET'])
def list_user_chamados(user_id):
    conn = get_connection()
    if not conn:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500

    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT numero, titulo, status 
        FROM chamado 
        WHERE usuario_id = %s
        ORDER BY data DESC
        """
        cursor.execute(query, (user_id,))
        chamados = cursor.fetchall()
        return jsonify({"chamados": chamados}), 200
    except Exception as e:
        return jsonify({"message": f"Erro ao buscar chamados: {str(e)}"}), 500
    finally:
        cursor.close()
        close_connection(conn)
