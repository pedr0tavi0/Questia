
from flask import Blueprint, render_template, redirect, url_for, flash,session
from app.forms import SignupForm, LoginForm
from functools import wraps

bp = Blueprint('main', __name__,template_folder='templates/main')

def verificar_autenticacao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session or session.get('username') is None:
            flash('Você precisa fazer login para acessar esta página.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/principal')
@verificar_autenticacao
def principal():
        return render_template('main/principal.html')
    
    
@bp.route('/usuario')
@verificar_autenticacao
def usuario():  
        return render_template('main/usuario.html')
   

@bp.route('/rank')
@verificar_autenticacao
def rank():
        return render_template('main/rank.html')
    