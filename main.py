from flask import Flask, Response

app = Flask(__name__)

@app.route("/painel/tiktokjisporyZZ5E4BwvQPexb6MJd7R6paF5X.txt")
def tiktok_verification():
    return Response("tiktok-domain-verification=tiktokjisporyZZ5E4BwvQPexb6MJd7R6paF5X", mimetype='text/plain')
