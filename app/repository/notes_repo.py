from SQLAlchemyError import sqlalchemy_error  
from models import Notes 



def create_note(title,created_at,content,user_id):
    note=Notes(title=title,created_at=created_at,content=content,user_id=user_id) 
    db.session.add(note)
    db.session.commit() 
    return note   

def get_noteby_id(note_id):
    return Notes.query.get(note_id)  
def get_all_notes():
    return Notes.query.all()
def get_notes_by_user_id(user_id):
    return Notes.query.filter_by(user_id=user_id).all() 


def update_note(note_id,**kwargs):
    note=Notes.query.get(note_id)  
    if not note:
        return None 
    for field,value in kwargs.items():
        if field not in [field_update_fields]:
            raise ValueError(f"field not allowed to be updated:{field}") 
        setattr(note,field,value)
        try:
            db.seession.commit()
        except SQLAlchemyError as e:
            db.session.rollback() 
            raise e  
        return note  

def delet_note(note_id):
    note=Notes.query.get(note_id)  
    if not note:
        raise ValueError(f"note with id {note_id} not found") 
    for field,value in kwargs.items():
        if field not in [field_update_fields]:
            raise ValueError(f"field not allowed to be updated:{field}") 
        setattr(note,field,value)
        try:
            db.seession.commit()
        except SQLAlchemyError as e:
            db.session.rollback() 
            raise e  
        return note
     