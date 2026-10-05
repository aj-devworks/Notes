from flask import jsonify,request,Blueprint 
from flask_jwt_extended import jwt_required,get_jwt_identity 
from app.services import create_note_service,get_note_service,get_notes_services,get_note_by_title_service,update_note_service,delete_note_service  



notes_bp=Blueprint('notes',__name__)


@notes_bp.route('/notes',methods=['POST']) 
@jwt_required()
def create_note():
    data = request.get_json(silent=True) or {} 
    title =data.get('title')
    content =data.get('content') 
    user_id = get_jwt_identity() 

    try:
        note = create_note_service(title,content,user_id) 
        if note:
            return jsonify({
                "message":"successfully saved",
                "id":note.id,
                "title":note.title, 
                "content":note.content
            }),201

    except ValueError as e:
        return jsonify ({"message":str(e)}),400 

@notes_bp.route('/notes/<int:id>',methods=['GET'])  
@jwt_required() 
def get_note(id):  
    identity_id = get_jwt_identity()
    try:
        notes = get_note_service(id) 

        if notes.user_id != identity_id:
            return jsonify({"message":"forbiden act"}),403
        return jsonify({
            "id":notes.id,
            "title":notes.title,
            "content":notes.content,
            "user_id":notes.user_id
        }),200 
    except ValueError as e:
        return jsonify ({
            "message":str(e)
        }),404
@notes_bp.route('/notes',methods=['GET'])  
def get_notes():
    notes = get_notes_services() 
    



         
            
        
            