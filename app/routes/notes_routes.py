from flask import jsonify,request,Blueprint 
from flask_jwt_extended import jwt_required,get_jwt_identity 
from app.services import create_note_service,get_note_service,get_notes_services,get_note_by_title_service,update_note_service,delete_note_service   
from app.schema.notes_schema import note,notes 



notes_bp=Blueprint('notes',__name__)


@notes_bp.route('/notes',methods=['POST']) 
@jwt_required()
def create_note():
id =get_jwt_identity() 
data =note.load(request.get_json()) 

    




         
            
        
            