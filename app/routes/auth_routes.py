from flask import Blueprint,jsonify,request 
from app.services.auth_service import sign_up_service,login_service 


user_auth =Blueprint('user_bp',__name__) 



@user_auth.route('/register',methods=['POST']) 
def create_user_routes():
    data = request.get_json(silent=True) or {}  
    user_name=data.get('user_name') 
    email=data.get('email') 
    password=data.get('password') 

   try:
    user = sign_up_service(user_name,email,password)  
   except ValueError as e:
    return jsonify({"message":str(e)}),400
   return jsonify({
    "id":user.id
    "user_name":user.user_name
    "email":user.email
    "message":"user has been successfully created"

   }),200




        

  
