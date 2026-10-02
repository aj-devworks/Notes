from extension import db,migrate,jwt,cors,bcrypt 
from flask import Flask  
from config import Config 
from app.routes import note_bp  
from app.routes.auth_routes import user_auth 


def creat_app():
    app = Flask(__name__)  
    app.config.from_object(Config)
    db.init_app(app) 
    migrate.init_app(app)  
    jwt.init_app(app) 
    cors.init_app(app) 
    bcrypt.init_app(app) 
    app.register_blueprint(note_bp) 
    app.register_blueprint(user_auth) 


    return app 
 

