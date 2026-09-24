from models import User 

allowed_update_fields=['password_hash'] 

def create_user(user_name,password):
    new_object=User(username=user_name,password_hash=password) 
    db.session.add(new_object)
    db.session.commit()
    return new_object 


def get_user_by_username(user_name):
    return User.query.filter_by(username=user_name).first() 
def get_user_by_id(user_id):
    return User.query.get(user_id)  
def get_all_users():
    return User.query.all()  


def update_user(user_id,**kwargs):
    user=User.query.get(user_id) 
    if not user:
        return None 
    for field,value in  kwargs.items():
        if field not in allowed_update_fields:
            raise ValueError(f"field not allowed to be updated:{field}")
        setattr(user,field,value) 
    db.session.commit() 
    return user  


