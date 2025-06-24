from flask import Flask, Response

app = Flask(__name__)

# Rota principal (opcional)
@app.route('/')
def home():
    return 'API do Auto-rells está ativa!'

# ✅ Rota de verificação do TikTok
@app.route('/painel/tiktokjisporyZZ5E4BwvQPexb6MJd7R6paF5X.txt')
def verificar_tiktok():
    return Response("tiktok-domain-verification=tiktokjisporyZZ5E4BwvQPexb6MJd7R6paF5X", mimetype="text/plain")

# Executar localmente (Render ignora isso, mas útil para testes locais)
if __name__ == '__main__':
    app.run(debug=True)
