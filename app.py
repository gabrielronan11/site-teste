import os

import gspread
import requests
from flask import Flask, request
from oauth2client.service_account import ServiceAccountCredentials
from tchan import ChannelScraper

TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID"]
SHEETS_JSON = os.environ["SHEETS_JSON"]

SHEETS_JSON = os.environ["SHEETS_JSON"]
with open("credenciais.json", mode="w") as arquivo:
  arquivo.write(SHEETS_JSON)
conta = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json")
api = gspread.authorize(conta)
planilha = api.open_by_key("1ZDyxhXlCtCjMbyKvYmMt_8jAKN5JSoZ7x3MqlnoyzAM")
sheet = planilha.worksheet("Sheet1")
app = Flask(__name__)
menu = """
<a href="/">Página Inicial</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""
@app.route("/")
def hello_world():
  return menu + "Olá, mundo! Esse é o meu site! (Gabriel Ronan)"
@app.route("/sobre")
def sobre():
  return menu + "Aqui vai o conteúdo da página sobre"
@app.route("/contato")
def contato():
  return menu + "Aqui vai o conteúdo da página contato"
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

    
menu = """
<a href="/">Página inicial</a> | <a href="/promocoes">PROMOÇÕES</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""
@app.route("/promocoes")
def promocoes():
  conteudo = menu + """
  Encontrei as seguintes promoções no <a href="https://t.me/promocoeseachadinhos">@promocoeseachadinhos</a>:
  <br>
  <ul>
  """
  for promocao in ultimas_promocoes():
    conteudo += f"<li>{promocao}</li>"
  return conteudo + "</ul>"
@app.route("/dedoduro")
def dedoduro():
  mensagem = {"chat_id": TELEGRAM_ADMIN_ID, "text": "Alguém acessou a página dedo duro!"}
  requests.post(f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage", data = mensagem)
  return "Mensagem enviada."

@app.route("/dedoduro2")
def dedoduro2():
  sheet.append_row(["Gabriel", "Ronan", "A partir do Flask"])
  return "Planilha escrita!"

@app.route("/telegram-bot")
def telegram_bot():
  update = request.json
  message = update["message"]["text"]
  chat_id = update["message"]["chat"]["id"]
  nova_mensagem = {"chat_id": chat_id, "text": message}
  requests.post(f"https://api.telegram.org./bot{token}/sendMessage", data=nova_mensagem)
  return "ok"

@app.route("/telegram-bot")
def telegram_bot():
  update = request.json
  chat_id = update["message"]["chat"]["id"]
  message = update["message"]["text"]
  nova_mensagem = {"chat_id": chat_id, "text": message}
  requests.post(f"https://api.telegram.org./bot{TELEGRAM_API_KEY}/sendMessage", data=nova_mensagem)
  return "ok"

