from app.services.notes_service import  create_note_service, get_note_service, update_note_service, delete_note_service 
from flask import request,jsonify,Blueprint 



note_bp=Blueprint("notes",__name__) 

@note_bp.route("/notes",methods=['POST'])
def create_note():
    data = request.get_json()
    title= data.get('title')
    content=data.get('content') 
    user_id=data.get('user_id') 
    try:
        note=create_note_service(title,content,user_id) 
        return jsonify({"id": note.id, "title": note.title, "content": note.content, "user_id": note.user_id}), 201 
    except Exception as e:
        return jsonify({"error": str(e)}), 400 
@note_bp.route('/notes/<int:note_id>',methods=['GET']) 
def get_note(note_id): 
    try:
        note=get_note_service(note_id) 
        if note:
            return jsonify({"id": note.id, "title": note.title, "content": note.content, "user_id": note.user_id}), 200 
        else:
            return jsonify({"error": "Note not found"}), 404 
    except Exception as e:
        return jsonify({"error": str(e)}), 400