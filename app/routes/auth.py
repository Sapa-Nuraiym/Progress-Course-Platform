from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from models import db
from models.user import User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.courses'))
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm_password')
        if password != confirm:
            flash('Құпиясөздер сәйкес келмейді!', 'error')
            return redirect(url_for('auth.register'))
        if User.query.filter_by(email=email).first():
            flash('Бұл email бұрыннан тіркелген!', 'error')
            return redirect(url_for('auth.register'))
        user = User(name=name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Сәтті тіркелдіңіз! Енді кіріңіз.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.courses'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user, remember=True)
            return redirect(url_for('main.courses'))
        flash('Email немесе құпиясөз қате!', 'error')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Жүйеден шықтыңыз.', 'info')
    return redirect(url_for('main.index'))