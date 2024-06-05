from flask import Blueprint, render_template, redirect, url_for, flash, session
from app.forms import SignupForm, LoginForm
from app.models.user import User
from app import db
from app.models.user import get_emblema_url
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Cadastrado, agora voce pode entrar para o Clã!")
        return redirect(url_for("auth.login"))
    return render_template("auth/signup.html", title="Sign Up", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("auth.login"))
        
        emblema_url = get_emblema_url(user.pontos)
        session["username"] = form.username.data
        session["emblema_url"] = emblema_url
        return redirect(url_for("main.principal"))
    return render_template("auth/login.html", title="Sign In", form=form)


@bp.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(
        url_for("main.index")
    )  # Redireciona para a rota principal após o logout
