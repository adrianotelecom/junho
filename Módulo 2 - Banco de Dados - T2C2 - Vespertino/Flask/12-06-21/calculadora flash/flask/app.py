from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    orc = 'orc'
    globin ='globin'
    feiticeira = 'feiticeira'

    soco = 'soco'
    arco = 'arco'
    espada = 'espada'

    img_orc = '../static/personagens/orc.png'
    img_globin = '../static/personagens/globin.png'
    img_feiticeira = '../static/personagens/feiticeira.png'

    img_soco = '../static/personagens/soco.png'
    img_arco = '../static/personagens/arco.png'
    img_espada = '../static/personagens/espada.png'


    return render_template(
        'index.html',
        orc = orc,
        globin = globin,
        feiticeira = feiticeira,

        soco = soco,
        arco = arco,
        espada = espada,

        img_orc = img_orc,
        img_globin = img_globin,
        img_feiticeira = img_feiticeira,

        img_soco = img_soco,
        img_arco = img_arco,
        img_espada = img_espada,
    )

if __name__ == "__main__":
    app.run(debug=True)
