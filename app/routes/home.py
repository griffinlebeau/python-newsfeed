from app.models import Post
from app.db import get_db
from flask import Blueprint, render_template
#Blueprint() lets us consolidate routes onto a single bp object that the parent app can register later
#bp corresponds to using the Router middleware of Express.js
bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/') #bp decorator to turn function into a route
def index():
  # get all posts
  db = get_db()
  # get_db returns a session connection thats tied to this route's context
  posts = db.query(Post).order_by(Post.created_at.desc()).all()
  # use query() method on connection object to query the Post model for all posts in descending order, with results saved in posts variable
  return render_template(
  'homepage.html',
  posts=posts
) # renders the template with posts data


@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>') #<id> represents the parameter from the URL
def single(id):
  # get single post by id
  db = get_db()
  #filter method on the connection object to specify the SQL WHERE clause
  post = db.query(Post).filter(Post.id == id).one()
  # pass the single post object to single-psot.html template 
  return render_template(
    'single-post.html',
    post=post
  )
  #once the template is rendered, and the response sent,
  #the context for this route terminates, and the teardown function closes the db connection 