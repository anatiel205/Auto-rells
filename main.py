from flask import Flask, render_template, request, redirect, url_for
from Crud import listar_usuarios, criar_usuario

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/painel')

@app.route('/painel')
def painel():
    usuarios = listar_usuarios()
    return render_template("painel.html", usuarios=usuarios)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        token = request.form['token']
        legenda = request.form['legenda']
        termo = request.form['termo']
        intervalo = int(request.form['intervalo'])
        criar_usuario(nome, token, legenda, termo, intervalo)
        return redirect(url_for('painel'))
    return render_template('adicionar.html')

if __name__ == '__main__':
    app.run(debug=True)
