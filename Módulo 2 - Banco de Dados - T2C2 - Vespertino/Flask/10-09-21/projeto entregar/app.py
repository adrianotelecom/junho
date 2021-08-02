from flask import Flask, app, render_template
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    nome ="Popeye"
    idade="120"
    humor=True
    imagem="https://i.gifer.com/1sC.gif"
    imagem2="https://blogopod.com/image/2009/popeye-vs-johnny-bravo.jpg"
    

    
    return render_template(
        "index.html" ,
        nome=nome,
        idade=idade,
        humor=humor,
        imagem=imagem,
        imagem2=imagem2
               
    )
@app.route("/Bravo", methods=["GET", "POST"])
def bravo():
    nome ="Popeye"
    idade="120"
    humor=False
    imagem="https://i.gifer.com/1sC.gif"
    imagem2="https://blogopod.com/image/2009/popeye-vs-johnny-bravo.jpg"

    return render_template(
        "index.html",
        nome=nome,
        idade=idade,
        humor=humor,
        imagem=imagem,
        imagem2=imagem2        
    )


if __name__=="__main__":
    app.run(debug=True)