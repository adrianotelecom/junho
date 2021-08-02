
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index ():
    return render_template('index.html')



# C - create
# R - Read - Leitura (Select)
# U - Update
# D - Delete

# Red () - Trabalhar com os dados mockados

registros = [
    {
        "id": 1,
        "nome": "La Casa de Papel",
        "imagem_URL":"https://i.ytimg.com/vi/Oqfh0dKHhT4/maxresdefault.jpg"
    },
    {
        "id": 2,
        "nome": "O Atirador",
        "imagem_URL":"https://assets0.minhaserie.com.br/uploads/editor_pictures/000/064/840/content_pic.jpg"
    },
    {
        "id": 3,
        "nome": "Lupin",
        "imagem_URL":"https://pipocasclub.com.br/wp-content/uploads/2021/01/Lupin-Netflix-Series-1.jpg"
    },
    {
        "id": 4,
        "nome": "Ponto Cego",
        "imagem_URL":"https://observatoriodocinema.uol.com.br/wp-content/uploads/2019/04/Blindspot.jpg"
    },
    {
        "id": 5,
        "nome": "Prisão de Mulheres",
        "imagem_URL":"https://claudia.abril.com.br/wp-content/uploads/2020/01/avlu-1.jpg"
    },
    {
        "id": 6,
        "nome": "Vis a Vis",
        "imagem_URL":"https://i.pinimg.com/originals/6b/86/f3/6b86f394b60a01ca7680fa9bb76635de.jpg"
    }
]

@app.route('/read')

def read_all():
    return render_template('read_all.html',registros=registros)

@app.route ('/read/<id_registro>')
def read_single(id_registro):
    return 'Em construção: Visualizar registro de ID'+ id_registro

if __name__ =="__main__":
    app.run(debug=True)