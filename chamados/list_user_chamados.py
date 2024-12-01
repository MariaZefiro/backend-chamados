from flask import Blueprint, jsonify
from db import get_connection, close_connection

list_user_chamados_bp = Blueprint('list_user_chamados', __name__)

@list_user_chamados_bp.route('/api/list_user_tickets/<int:colaborador_id>', methods=['GET'])
def list_user_tickets(colaborador_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        if not conn:
            raise Exception("Não foi possível obter uma conexão com o banco de dados.")

        cursor = conn.cursor(dictionary=True)
        
        query = """
          SELECT 
            c.id AS ticket_id,
            c.numero,
            c.titulo,
            c.descricao,
            c.setor,
            c.data,
            c.status,
            c.prioridade,
            c.tipo_de_problema,
            c.especificacao_problema,
            u.nome AS usuario_nome
        FROM 
            chamado AS c
        JOIN 
            colaboradores_chamados AS cc ON c.id = cc.chamado_id
        JOIN 
            colaboradores AS col ON cc.colaborador_id = col.id
        JOIN 
            usuarios AS u ON c.usuario_id = u.id
        WHERE 
            cc.colaborador_id = %s;
        """
        cursor.execute(query, (colaborador_id,))
        tickets = cursor.fetchall()

        return jsonify({"tickets": tickets})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            if conn.is_connected():
                close_connection(conn)
            else:
                print("A conexão não está ativa.")

@list_user_chamados_bp.route('/api/list_chamado_usuario/<int:user_id>', methods=['GET'])
def list_chamado_usuario(user_id):
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