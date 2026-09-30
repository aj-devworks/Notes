from models import User  
from extension import db 

allowed_update_fields=['password_hash','email','user_name'] 

def create_user_repo(user_name,email,password): 
    new_user = User(user_name=user_name,email=email) 
    new_user.set_password(password) 
    db.session.add(new_user) 
    db.session.commit() 
    return new_user 
    


def get_user_by_email(email):
    new_user = User.query.filter_by(email=email).first() 
    return new_user  