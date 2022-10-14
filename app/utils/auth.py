from flask import session, redirect
from functools import wraps

def login_required(func):
  @wraps(func) #preserves original name and arguments 
  def wrapped_function(*args, **kwargs):
    # if logged in, call original function with original arguments
    if session.get('loggedIn') == True:
      return func(*args, **kwargs)

    return redirect('/login')
  
  return wrapped_function