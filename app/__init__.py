from extension import db,migrate,jwt,cors,bcrypt 
from flask import Flask  
from config import Config


def creat_app():
    app = Flask(__name__)  
    app.config.from_object(Config)
    db.init_app(app) 
    migrate.init_app(app)  
    jwt.init_app(app) 
    cors.init_app(app) 
    bcrypt.init_app(app)

    return app 
 

