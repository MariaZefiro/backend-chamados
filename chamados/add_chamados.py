from flask import Blueprint, request, jsonify
from mysql.connector import Error
from db import get_connection, close_connection
from flask_socketio import SocketIO
from datetime import datetime

def create_add_chamado_blueprint(socketio: SocketIO):
    add_chamado_bp = Blueprint('add_chamado', __name__)

    @add_chamado_bp.route('/api/add_chamado', methods=['POST'])
    def add_chamado():
        data = request.get_json()

        usuario_id = data.get('userId')
        setor = data.get('sector')
        tipo_de_problema = data.get('category')
        especificacao_problema = data.get('subCategory')
        titulo = data.get('title')
        descricao = data.get('description')

        if not all([usuario_id, setor, tipo_de_problema, titulo, descricao]):
            return jsonify({"message": "Dados incompletos"}), 400

        conn = get_connection()
        if not conn:
            return jsonify({"message": "Erro ao conectar ao banco de dados"}), 500

        cursor = conn.cursor()
        try:
            setor_prefix = setor[:3].upper()
            cursor.execute("SELECT COUNT(*) + 1 FROM chamado WHERE setor = %s", (setor,))
            sequencial = cursor.fetchone()[0]
            numero = f"#{setor_prefix}{sequencial:04d}"
            data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            query = """
            INSERT INTO chamado (numero, usuario_id, setor, tipo_de_problema, especificacao_problema, titulo, descricao, data, status, prioridade)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'Aberto', 'A definir')
            """
            cursor.execute(query, (numero, usuario_id, setor, tipo_de_problema, especificacao_problema, titulo, descricao, data_atual))
            conn.commit()

            socketio.emit('novo_chamado', {
                "message": "Novo chamado adicionado",
                "numero": numero,
                "titulo": titulo,
                "setor": setor,
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  
                "status": "Aberto",
                "prioridade": "A definir"
            })

            return jsonify({"message": "Chamado criado com sucesso!"}), 200
        except Error as e:
            return jsonify({"message": f"Erro ao salvar chamado: {str(e)}"}), 500
        finally:
            cursor.close()
            close_connection(conn)

    return add_chamado_bp
