from flask import Blueprint, render_template
#Blueprint() lets us consolidate routes onto a single bp object that the parent app can register later
#bp corresponds to using the Router middleware of Express.js
bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/') #bp decorator to turn function into a route
def index(): 
  return render_template('homepage.html') #route response with template

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>') #<id> represents the parameter from the URL
def single(id):
  return render_template('single-post.html')