from flask import Flask
from tchan import ChannelScraper
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
@app.route("/ultimaspromocoes")
def ultimas_promocoes():
  scraper = ChannelScraper()
  contador = 0
  resultado = []
  for message in scraper.messages("promocoeseachadinhos"):
    contador += 1
    texto = message.text.strip().splitlines()[0]
    resultado.append(f"{message.created_at} {texto}")
    if contador == 10:
      return resultado
