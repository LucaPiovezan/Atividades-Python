from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

usuarios = [
    {'usuario': 'luca',    'senha': '1234',        'nome': 'Luca Piovezan'},
    {'usuario': 'marcos',  'senha': 'cotemig2026',  'nome': 'Marcos'},
    {'usuario': 'janaina', 'senha': 'cotemig2026',  'nome': 'Janaina'},
]

def verificar_login(usuario, senha):
    for u in usuarios:
        if u['usuario'] == usuario and u['senha'] == senha:
            return u['nome']
    return None


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None

    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha   = request.form.get('senha')
        nome    = verificar_login(usuario, senha)

        if nome:
            return render_template('bemvindo.html', nome=nome, usuario=usuario)
        else:
            erro = 'Usuário ou senha incorretos.'

    return render_template('login.html', erro=erro)


if __name__ == '__main__':
    app.run(debug=True)