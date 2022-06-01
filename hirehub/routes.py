from flask import Blueprint, render_template, url_for, flash, redirect
from hirehub.forms import RegistrationForm, LoginForm
from hirehub.models import User, Post

users = Blueprint('users', __name__)
@users.route('/')
@users.route('/home')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@users.route('/about')
def about():
    return render_template('about.html', title = 'About')


