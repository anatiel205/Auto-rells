from flask import Flask, render_template, request
from Crud import criar_tabela, salvar_usuario, buscar_usuario

app = Flask(__name__)
criar_tabela()  # Garante que a tabela existe

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/painel", methods=["POST"])
def painel():
    token = request.form.get("token")
    legenda = request.form.get("legenda")
    tempo = int(request.form.get("tempo"))
    termo = request.form.get("termo")

    salvar_usuario(token, legenda, tempo, termo)
    user = buscar_usuario(token)

    return render_template("painel.html", usuario=user)

if __name__ == "__main__":
    app.run(debug=True)
