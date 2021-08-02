from logging import debug
from flask import Flask
app = Flask (__name__)

@app.route("/")
def home():
    return "Hello, Flask !"

@app.route("/rota2")
def rota2():
    return"<h1> Essa é a página da segunda rota</h1>"

@app.route("/blue")
def blue():
    return"<h1> Eu sou Bluemer</h1>"

@app.route("/blue/bluemer")
def bluemer():
    return"<h1> No caminho do sucesso</h1>"
if __name__ == "__main__":
    app.run(debug=True)
