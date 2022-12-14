from app.utils import filters
from app.routes import home, dashboard, api
#we can import home directly from routes package because its __init__.py file imported the blueprint
from flask import Flask
from app.db import init_db

def create_app(test_config=None):
    # set up app config
    app = Flask(__name__, static_url_path='/') #declare a new app variable
    app.url_map.strict_slashes = False #app should serve any static resources from the root dir and not from default /stsatic dir, also sets trailing slashes to option (so /dashboard and /dashboard/ load the same route)
    app.config.from_mapping( #app should use the key defined here when creating server-side sessions
        SECRET_KEY='super_secret_key'
    )

    @app.route('/hello') #decorator that turns the hello() function into a route
    def hello(): #inner function that returns a string when called
            return 'hello world' #the functions return becomes the route's response
    app.register_blueprint(home) #registers our home routes
    app.register_blueprint(dashboard) #register dashboard routes
    app.register_blueprint(api) #any routes we define in the api.py module will automatically become part of the Flask app and have a prefix of /api
    init_db(app)#included app paramter for proper close db functionality 

    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural


    return app