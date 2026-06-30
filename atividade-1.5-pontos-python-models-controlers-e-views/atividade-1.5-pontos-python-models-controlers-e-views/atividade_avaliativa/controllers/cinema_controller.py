# Cenário: B - Cinema
from flask import Blueprint, redirect, render_template, request, url_for
from datetime import datetime

from models import Filme, Sala, Sessao, db

cinema_bp = Blueprint("cinema", __name__, url_prefix="/cinema")


@cinema_bp.route("/")
def index():
    sessoes = Sessao.query.all()
    return render_template("cinema/lista_sessoes.html", sessoes=sessoes)


@cinema_bp.route("/sessao/cadastrar", methods=["GET", "POST"])
def cadastrar_sessao():
    filmes = Filme.query.all()
    salas = Sala.query.all()

    if request.method == "POST":
        filme_id = request.form.get("filme_id")
        sala_id = request.form.get("sala_id")
        data_hora_str = request.form.get("data_hora")
        preco = request.form.get("preco")

        data_hora = datetime.strptime(data_hora_str, "%Y-%m-%dT%H:%M")

        nova_sessao = Sessao(
            filme_id=filme_id,
            sala_id=sala_id,
            data_hora=data_hora,
            preco=float(preco)
        )
        
        db.session.add(nova_sessao)
        db.session.commit()

        return redirect(url_for("cinema.index"))

    return render_template(
        "cinema/formulario_sessao.html",
        filmes=filmes,
        salas=salas,
    )
