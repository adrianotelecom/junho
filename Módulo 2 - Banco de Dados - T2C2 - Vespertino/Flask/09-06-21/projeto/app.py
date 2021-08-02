from logging import debug
from flask import Flask, render_template
app = Flask (__name__)

@app.route("/")
def index():
    nome = "Pica pau"
    hp = 2000

    exibir_imagem = True
    imagem = "https://img1.picmix.com/output/pic/normal/7/6/4/0/5030467_619a5.gif"

    return render_template(
    "index.html",
    nome = nome,
    hp = hp,
    exibir_imagem = exibir_imagem,
    imagem = imagem
    )
if __name__ == "__main__":
    app.run(debug=True)