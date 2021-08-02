from logging import debug
from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/", methods=('GET','POST'))

def home():
    if request.method =="POST":
        usuario_nome = request.form["usuario_nome"]
        usuario_sobrenome = request.form["usuario_sobrenome"]
        apenas_uma_opcao = request.form["apenas_uma_opcao"]
        varias_opcoes = request.form["varias_opcoes"]

        print(f'Nome do usuário: {usuario_nome}')
        print(f'Nome do usuário: {usuario_sobrenome}')
        print(f'Apenas uma opção: {apenas_uma_opcao}')
        print(f'Várias opções: {varias_opcoes}')

    return render_template(
        
        
        
        "index.html")


if __name__ == ("__main__"):
    app.run(debug=True)