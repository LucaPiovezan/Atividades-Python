from flask import Blueprint, jsonify, request
from models import Filme, Sala, Sessao, db

api_v1_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")


@api_v1_bp.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "API está funcionando"}), 200


@api_v1_bp.route("/filmes", methods=["GET"])
def listar_filmes():
    filmes = Filme.listar()
    return jsonify([{
        "id": f.id,
        "titulo": f.titulo,
        "duracao_min": f.duracao_min,
        "classificacao": f.classificacao
    } for f in filmes]), 200


@api_v1_bp.route("/filmes/<int:filme_id>", methods=["GET"])
def obter_filme(filme_id):
    filme = Filme.query.get_or_404(filme_id)
    return jsonify({
        "id": filme.id,
        "titulo": filme.titulo,
        "duracao_min": filme.duracao_min,
        "classificacao": filme.classificacao
    }), 200


@api_v1_bp.route("/filmes", methods=["POST"])
def criar_filme():
    dados = request.get_json()
    filme = Filme(
        titulo=dados["titulo"],
        duracao_min=dados["duracao_min"],
        classificacao=dados["classificacao"],
    )
    db.session.add(filme)
    db.session.commit()
    return jsonify({"id": filme.id, "mensagem": "Filme criado com sucesso"}), 201


@api_v1_bp.route("/salas", methods=["GET"])
def listar_salas():
    salas = Sala.listar()
    return jsonify([{
        "id": s.id,
        "numero": s.numero,
        "capacidade": s.capacidade
    } for s in salas]), 200


@api_v1_bp.route("/sessoes", methods=["GET"])
def listar_sessoes():
    sessoes = Sessao.listar_com_detalhes()
    return jsonify([{
        "id": s.id,
        "filme": s.filme.titulo,
        "sala": s.sala.numero,
        "data_hora": s.data_hora.isoformat(),
        "preco": s.preco
    } for s in sessoes]), 200


@api_v1_bp.route("/sessoes", methods=["POST"])
def criar_sessao():
    dados = request.get_json()
    from datetime import datetime
    sessao = Sessao(
        filme_id=dados["filme_id"],
        sala_id=dados["sala_id"],
        data_hora=datetime.fromisoformat(dados["data_hora"]),
        preco=dados["preco"],
    )
    db.session.add(sessao)
    db.session.commit()
    return jsonify({"id": sessao.id, "mensagem": "Sessão criada com sucesso"}), 201
