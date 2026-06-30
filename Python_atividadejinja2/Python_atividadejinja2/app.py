from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    estudante = "Estudante "
    return render_template('index.html', nome=estudante)

@app.route('/alunos')
def mostrar_alunos():
    lista_alunos = [
        {"nome": "aaaaa", "idade": 18},
        {"nome": "bbbb", "idade": 20},
        {"nome": "cccc", "idade": 22}
    ]

    return render_template('alunos.html', alunos=lista_alunos)

@app.route('/usuario')
def perfil_usuario():
    dados_usuario = {
        "nome": "aaaaa",
        "email": "aaaa@email.com"
    }

    return render_template('usuario.html', usuario=dados_usuario)

@app.route('/lista_nomes')
def exibir_nomes():
    lista = ["aaaaaa", "bbbbbb", "ccccc", "ddddd"]

    return render_template('lista_nomes.html', nomes=lista)

@app.route('/notas')
def exibir_notas():
    notas_alunos = [
        {"nome": "aaaaa", "nota": 8.5},
        {"nome": "bbbbb", "nota": 5.0},
        {"nome": "ccccc", "nota": 7.0}
    ]

    return render_template('notas.html', alunos=notas_alunos)

if __name__ == '__main__':
    app.run(debug=True)