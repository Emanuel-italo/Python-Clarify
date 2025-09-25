r"""
 _____                                  _ 
| ____|_ __ ___   __ _ _ __  _   _  ___| |
|  _| | '_ ` _ \ / _` | '_ \| | | |/ _ \ |
| |___| | | | | | (_| | | | | |_| |  __/ |
|_____|_| |_| |_|\__,_|_| |_|\__,_|\___|_|

Autor: Emanuel Italo
Versão: 0.0.0.1
Data: 25/09/2025
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Bem-vindo à minha página</h1>"

@app.route("/sobre")
def informacoes():
    return "<marquee> Emanuel italo leal </marquee>"

@app.route("/saudacao/<nome>")
def saudacao(nome):
    return f"<h1> Bem vindo </h1>{nome}"

if __name__ == "__main__":
    app.run(debug=True)
