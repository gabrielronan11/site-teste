from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
  return "Olá, mundo. Aqui quem fala é o (Gabriel Ronan)"
