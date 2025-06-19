from flask import Flask, render_template, request, redirect, url_for
from Crud import criar_usuario, listar_usuarios

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/painel')
def painel():
    usuarios = listar_usuarios()
    return render_template('painel.html', usuarios=usuarios)

@app.route('/criar_usuario', methods=['POST'])
def criar():
    nome = request.form['nome']
    token = request.form['token']
    legenda = request.form['legenda']
    termo = request.form['termo']
    intervalo = request.form['intervalo']
    criar_usuario(nome, token, legenda, termo, intervalo)
    return redirect(url_for('painel'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
