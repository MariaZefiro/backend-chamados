from flask import Blueprint, jsonify, request
from db import get_connection, close_connection

list_artigos_bp = Blueprint('list_artigos', __name__)

@list_artigos_bp.route('/api/list_artigos', methods=['GET'])
def list_artigos(): 
    conn = get_connection()
    if not conn:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500

    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM artigos;"
        cursor.execute(query)
        artigos = cursor.fetchall()

        return jsonify({"artigos": artigos}), 200
    except Exception as e:
        return jsonify({"message": f"Erro ao buscar artigos: {str(e)}"}), 500
    finally:
        cursor.close()
        close_connection(conn)