from flask import Blueprint, jsonify, request
from db import get_connection, close_connection

edit_chamado_bp = Blueprint('edit_chamado', __name__)

@edit_chamado_bp.route('/api/edit_chamado', methods=['POST'])
def salvar_edicao_chamado():
    data = request.json
    chamado_id = data.get('id')
    status = data.get('status')
    prioridade = data.get('prioridade')
    colaboradores = data.get('colaboradores', [])

    if not chamado_id:
        return jsonify({"message": "ID do chamado é obrigatório"}), 400

    conn = get_connection()
    if not conn:
        return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500

    cursor = conn.cursor()
    try:
        # Atualizar apenas os campos não nulos
        update_fields = []
        update_values = []

        if status is not None:
            update_fields.append("status = %s")
            update_values.append(status)
        
        if prioridade is not None:
            update_fields.append("prioridade = %s")
            update_values.append(prioridade)
        
        if update_fields:
            query_update_chamado = f"""
                UPDATE chamado
                SET {', '.join(update_fields)}
                WHERE id = %s;
            """
            cursor.execute(query_update_chamado, (*update_values, chamado_id))

        # Atualizar colaboradores se fornecido
        if colaboradores:
            query_delete_colaboradores = """
                DELETE FROM colaboradores_chamados
                WHERE chamado_id = %s;
            """
            cursor.execute(query_delete_colaboradores, (chamado_id,))

            query_insert_colaboradores = """
                INSERT INTO colaboradores_chamados (chamado_id, colaborador_id)
                VALUES (%s, %s);
            """
            for colaborador_id in colaboradores:
                cursor.execute(query_insert_colaboradores, (chamado_id, colaborador_id))

        conn.commit()

        # Retornar o chamado atualizado
        query_fetch_chamado = """
            SELECT c.id, c.status, c.prioridade, c.titulo, c.setor, c.usuario_id, c.data
            FROM chamado c
            WHERE c.id = %s;
        """
        cursor.execute(query_fetch_chamado, (chamado_id,))
        chamado_atualizado = cursor.fetchone()

        return jsonify({"chamado": chamado_atualizado}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"message": f"Erro ao salvar as alterações: {str(e)}"}), 500
    finally:
        cursor.close()
        close_connection(conn)