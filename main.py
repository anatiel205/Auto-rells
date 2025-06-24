from flask import Flask, Response

app = Flask(__name__)

@app.route('/tiktok-verification.txt')
def tiktok_verification():
    return Response("tiktok-domain-verification= jisporyZZ5E4BwvQPexb6MJd7R6paF5X", mimetype='text/plain')
