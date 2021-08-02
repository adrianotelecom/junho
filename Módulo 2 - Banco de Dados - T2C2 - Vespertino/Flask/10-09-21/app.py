from logging import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    nome_jogador ="Jorginho Betão Silva"
    premio =True
    return render_template(
        "index.html" ,
        nome_jogador=nome_jogador,
        premio=premio
    )

if __name__=="__main__":
    app.run(debug=True)
