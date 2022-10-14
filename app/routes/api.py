from flask import Blueprint, request, jsonify, session
import sys
#request is a global object like g that contains information about the request itself
from app.models import User
from app.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    #data is a Python dictionary data type
    #must use bracket notation - data['property'] to access properties of a dictionary
  data = request.get_json()
  db = get_db()
  try:
    # attempt creating a new user
    newUser = User(
      username = data['username'],
      email = data['email'],
      password = data['password']
    )
    db.add(newUser)
    db.commit()
  except:
    print(sys.exe_info()[0])
    #an assertion error is thrown when a custom validation fails
    #an integrity erro ris thrown when something specific to MySQL like a UNIQUE constraint fails
    # insert failed, so send error to front end
    db.rollback() #resolves issue of pending database connections in the event of insertion failure
    return jsonify(message = 'Signup failed'), 500  
  session.clear() #clears any existing session data
  session['user_id'] = newUser.id #create session property to aid in future db queries
  session['loggedIn'] = True #create boolean session property that templates will use to conditionally render elements 
  return jsonify(id = newUser.id)
  #sessions can only be created in FLask if you've defined a secret key

@bp.route('/users/logout', methods=['POST'])
def logout():
  # remove session variables
  session.clear()
  return '', 204

@bp.route('/users/login', methods=['POST'])
def login():
  data = request.get_json()
  db = get_db()
  try: #first step is to check whether the user's posted email address exists in the db
    user = db.query(User).filter(User.email == data['email']).one()
  except:
    print(sys.exc_info()[0])

    return jsonify(message = 'Incorrect credentials'), 400
  if user.verify_password(data['password']) == False:
    return jsonify(message = 'Incorrect credentials'), 400
  session.clear()
  session['user_id'] = user.id
  session['loggedIn'] = True

  return jsonify(id = user.id)
  