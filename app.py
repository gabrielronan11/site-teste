from flask import Flask
app = Flask(__name__)
menu = """
<a href="/">Página Inicial</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""
@app.route("/")
def hello_world():
  return "Olá, mundo! Esse é o meu site! (Gabriel Ronan)"
@app.route("/sobre")
def sobre():
  return "Aqui vai o conteúdo da página sobre"
@app.route("/contato")
def contato():
  return "Aqui vai o conteúdo da página contato"
