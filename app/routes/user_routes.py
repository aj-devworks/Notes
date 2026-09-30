from flask import request,jsonify,Blueprint 
from app.services.user_servcies import create_user_service,get_user_service,update_user_service,delete_user_service ,get_users_service




user_bp=Blueprint('user',__name__) 


@user_bp.route('/users',methods=['POST']) 
def create_user():
    data = request.get_json() 
    user_name=data.get('user_name')
    password=data.get('password')
    email=data.get('email')


    try:
        user=create_user_service(user_name,password,email) 
        return jsonify({'id':user.id,'user_name':user.user_name,'email':user.email}),201  
    except ValueError as e:
        return jsonify({'error':str(e)}),400
@user_bp.route('/users',methods=['GET']) 
def get_users():
    try:
        users = get_users_service() 
        return jsonify ([{'id':user.id,'user_name':user.user_name,'email':user.email }for user in users]),201 

    except ValueError as e:
        return jsonify ({'error':str(e)}),400 

@user_bp.route('/users/<int:user_id>',methods=['GET']) 
def get_user(user_id):
    try:
        user=get_user_service(user_id) 
        return jsonify({'id':user.id,'user_name':user.user_name,'email':user.email}),201 
    except ValueError as e:
        return jsonify ({"error":str(e)}),400   
@user_bp.route('/users/<int:user_id>',methods=['PUT'])  
def update_user(user_id):
    data = request.get_json() 
    try:
        user = update_user_service(user_id,**data) 
        return jsonify ({'id':user.id,'user_name':user.user_name,'email':user.email})  
    except ValueError as e:
        return jsonify({'error':str(e)}),400  
@user_bp.route('/users/<int:user_id>',methods=['DELETE'])   
def delet_user(user_id): 
    try:
        deleted=delete_user_service(user_id)
        return jsonify({"message":"successfully deleted"})  
    except ValueError as e:
        return jsonify ({"message":str(e)}),400
    

