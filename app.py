from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def pagina_inicial():
    return "Gustavo Blima - Iniciando site"