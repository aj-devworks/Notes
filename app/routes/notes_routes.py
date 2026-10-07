from app.services.notes_service import create_note_service 
from flask import Blueprint,request,jsonify 
from flask_jwt_extended import jwt_required,get_jwt_identity 
from app.schema import NoteSchema


notes_bp=Blueprint("notes",__name__,)  


@notes_bp.route("/notes",methods=["POST"]) 
@jwt_required() 
def create_note(): 
    id = get_jwt_identity() 
    try:
        data =note_schema.load(request.get_json())  
        tite = data.get("title")
        content = data.get("content") 
        nw_note=create_note_service(title,content,id)
        return note_schema.dump(nw_note),201 
    except ValidatioError as err:
        return jsonify({"message":err.messages}),400 
    except ValueError as e:
        return jsonify({"message":str(e)}),400  

