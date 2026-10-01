from app.repository.user_repo import create_user_repo,get_user_by_email 
from flask_jwt_extended import create_access_token  




def sign_up_service(user_name,email,password):  
    if not user_name or not email or not password:

        raise ValueError('all fields are required')   

    return create_user_repo(user_name,email,password)  
def login_service(password,email): 

    user = get_user_by_email(email) 
    if not user :
        raise ValueError("invalid email or password") 

    if not user.check_password_hash(password): 
        raise ValueError("invalid email or password")  

    token = create_access_token(identity=user.id) 
    return ('token':token,'user_id':user.id ,'user_name':user.user_name)  



     







