from flask import Blueprint, jsonify, request
from db import get_connection, close_connection

list_chamados_bp = Blueprint('list_chamados', __name__)

@list_chamados_bp.route('/api/list_chamados', methods=['GET'])
def list_user_chamados():
    setor = request.args.get('setor')  
    conn = get_connection()
    if not conn:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500

    cursor = conn.cursor(dictionary=True)
    try:
        query = """
            SELECT 
                c.id, 
                c.numero, 
                u.nome AS usuario_nome, 
                c.setor, 
                c.tipo_de_problema, 
                c.especificacao_problema, 
                c.titulo, 
                c.descricao, 
                c.data, 
                c.status,
                c.prioridade
            FROM chamado c
            INNER JOIN usuarios u ON c.usuario_id = u.id
        """
        if setor:
            query += " WHERE c.setor = %s"
            cursor.execute(query, (setor,))
        else:
            cursor.execute(query)

        chamados = cursor.fetchall()
        return jsonify({"chamados": chamados}), 200
    except Exception as e:
        return jsonify({"message": f"Erro ao buscar chamados: {str(e)}"}), 500
    finally:
        cursor.close()
        close_connection(conn)