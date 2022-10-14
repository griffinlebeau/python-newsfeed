from app.routes import home, dashboard
#we can import home directly from routes package because its __init__.py file imported the blueprint
from flask import Flask

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


    return app