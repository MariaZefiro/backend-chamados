from flask import Blueprint, jsonify, request
from db import get_connection, close_connection

list_colaboradores_bp = Blueprint('list_colaboradores', __name__)

@list_colaboradores_bp.route('/api/list_colaboradores', methods=['GET'])
def list_colaboradores(): 
    conn = get_connection()
    if not conn:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500

    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM colaboradores;"
        cursor.execute(query)
        colaboradores = cursor.fetchall()

        return jsonify({"colaboradores": colaboradores}), 200
    except Exception as e:
        return jsonify({"message": f"Erro ao buscar colaboradores: {str(e)}"}), 500
    finally:
        cursor.close()
        close_connection(conn)