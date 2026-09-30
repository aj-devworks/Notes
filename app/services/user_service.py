from app.repository.user_repo import create_user_repo,get_user_by_email 




def create_service_user(user_name,email,password):  
    if not user_name or not email or not password:
        raise ValueError('all fields are required')  
    return create_user_repo(user_name,email,password) 
    
        

def get_user_service_email(email):  
    user = get_user_by_email(email) 
    if not user:
        raise ValueError('email donot exists') 
    return user


