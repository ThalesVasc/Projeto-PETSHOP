<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
=======
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
>>>>>>> 5fc6e510c543278a6866ac47e7d200d2f8013872

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
<<<<<<< HEAD
app.secret_key = 'sua_chave_secreta'  # Chave para mensagens de flash

db = SQLAlchemy(app)


=======

db = SQLAlchemy(app)

>>>>>>> 5fc6e510c543278a6866ac47e7d200d2f8013872
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
<<<<<<< HEAD
    senha = db.Column(db.String(200), nullable=False)  # Adicionando campo de senha
=======
>>>>>>> 5fc6e510c543278a6866ac47e7d200d2f8013872

# Criar as tabelas no banco de dados
with app.app_context():
    db.create_all()

@app.route('/')
def entrar():
    return render_template('entrar.html')

<<<<<<< HEAD

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')

        # Verificar se o email existe no banco de dados
        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.senha, senha):  # Verifica se a senha está correta
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('dashboard'))  # Página de redirecionamento após login
        else:
            flash('Email ou senha incorretos.', 'danger')

=======
@app.route('/login', methods=['GET', 'POST'])
def login():
>>>>>>> 5fc6e510c543278a6866ac47e7d200d2f8013872
    return render_template('login.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/CadastroCliente', methods=['GET', 'POST'])
def cliente():
    return render_template('cliente.html')

@app.route('/CadastroPet', methods=['GET', 'POST'])
def pet():
    return render_template('pet.html')

@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if request.method == 'POST':
        nome = request.form.get('nome_completo')
        genero = request.form.get('genero')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')

        # Criar um novo usuário no banco de dados
        novo_usuario = Usuario(
            nome=nome,
            genero=genero,
            email=email,
            telefone=telefone,
            endereco=endereco
        )
        db.session.add(novo_usuario)
        db.session.commit()

        # Redireciona para a página de perfil e passa as informações do novo usuário
        return render_template('perfil.html', nome=nome, genero=genero, email=email, telefone=telefone, endereco=endereco)

    # Caso seja um GET, buscamos os dados de todos os usuários cadastrados
    usuarios = Usuario.query.all()
    return render_template('perfil.html', usuarios=usuarios)


@app.route('/PerfilPet', methods=['POST'])
def perfil_pet():
    nome = request.form.get('nome')
    especie = request.form.get('especie')
    raca = request.form.get('raca')
    idade = request.form.get('idade')
    sexo = request.form.get('sexo')
    cor = request.form.get('cor')
    peso = request.form.get('peso')
    responsavel = request.form.get('responsavel')

    return render_template('perfilPet.html', nome=nome, especie=especie, raca=raca, idade=idade, sexo=sexo, cor=cor, peso=peso, responsavel=responsavel)

@app.route('/HomePage', methods=['GET', 'POST'])
def HomePage():
    return render_template('HomePage.html')

@app.route('/loja', methods=['GET', 'POST'])
def loja():
    return render_template('/loja.html')

if __name__ == '__main__':
    app.run(debug=True)
