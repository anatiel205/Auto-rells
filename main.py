from flask import Flask, render_template, request, redirect
from Crud import criar_tabela, criar_usuario, listar_usuarios

app = Flask(__name__)

# Garante que a tabela será criada ao iniciar
criar_tabela()

@app.route("/")
def index():
    usuarios = listar_usuarios()
    return render_template("index.html", usuarios=usuarios)

@app.route("/painel")
def painel():
    return render_template("painel.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    token = request.form["token"]
    legenda = request.form["legenda"]
    termo = request.form["termo"]
    intervalo = int(request.form["intervalo"])

    criar_usuario(nome, token, legenda, termo, intervalo)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
