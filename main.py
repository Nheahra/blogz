from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import cgi

app = Flask(__name__)
app.config(['DEBUG']) = True

class User(db.model):
    id = db.column(db.Integer, primary_key=True)
    username = db.column(db.String(120))
    password = db.Column(db.String(120))
    blogs = db.relationship('Blog', backref='owner')

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Blog(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(5000))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, body, owner):
        self.title = title
        self.body = body
        self.owner = owner

@app.route('/allPosts')
def getPosts ():
    blog = Blog.query.all()
    return render_template('allPosts.html', blog=blog)

@app.route('/signup')
def sign_up ():
    return render_template('signup.html')

@app.route('/')
def home ():
    blog = Blog.query.all()
    return render_template('home.html', blog=blog)