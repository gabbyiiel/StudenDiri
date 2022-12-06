from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bayotka?'
    
    from.views import views
    from.auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app