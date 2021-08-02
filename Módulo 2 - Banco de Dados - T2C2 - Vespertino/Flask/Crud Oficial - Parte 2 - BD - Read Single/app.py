from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Banco de dados (Database)

user='rcmuzfky'
password='sSOvZIR1dVS7L4ZLM-LgQnSLBeOveOPE'
host='tuffi.db.elephantsql.com'
database='rcmuzfky'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secreta'

db = SQLAlchemy(app)

# Filmes db

# Integer = int (Dbeaver)
# String = varchar (Dbeaver)
# nullable = not null (Dbeaver)

class Filmes(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(255),nullable=False)
    imagem_url= db.Column(db.String(255),nullable=False)  
    
    def __init__(self,nome, imagem_url):
        self.nome = nome
        self.imagem_url=imagem_url
    
    @staticmethod
    def read_all():
        # Select * from filmes order by id asc
        return Filmes.query.order_by(Filmes.id.asc()).all()


    @staticmethod
    def read_single(registro_id):
        # Select * from filmes where id=1
        return Filmes.query.get(registro_id)


#Rotas

@app.route('/')

def index ():
    return render_template('index.html')

#Read

@app.route('/read')

def read_all():
    registros = Filmes.read_all()

    return render_template('read_all.html',registros=registros)

@app.route ('/read/<registro_id>')
def read_single(registro_id):
    registro = Filmes.read_single(registro_id)
    print(registro)
    
    return render_template('read_single.html', registro = registro)

if __name__ =="__main__":
    app.run(debug=True)