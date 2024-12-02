from flask import Blueprint, jsonify, request
from db import get_connection, close_connection
from datetime import datetime

add_artigos_bp = Blueprint('add_artigos', __name__)

@add_artigos_bp.route('/api/add_artigos', methods=['POST'])
def add_artigos():
    conn = get_connection()
    if not conn:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500

    data = request.json 
    titulo = data.get("titulo")
    descricao = data.get("descricao")
    data_publicacao = datetime.now().strftime('%Y-%m-%d')

    if not titulo or not descricao:
        return jsonify({"message": "Título e descrição são obrigatórios"}), 400

    cursor = conn.cursor()
    try:
        query = """
        INSERT INTO artigos (titulo, descricao, data_publicacao)
        VALUES (%s, %s, %s);
        """
        cursor.execute(query, (titulo, descricao, data_publicacao))
        conn.commit()

        return jsonify({"message": "Artigo adicionado com sucesso"}), 200
    except Exception as e:
        return jsonify({"message": f"Erro ao adicionar artigo: {str(e)}"}), 500
    finally:
        cursor.close()
        close_connection(conn)