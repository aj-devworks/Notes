from app.models import NOtes 



def create_note(title:str,content:str,user_id:int):             
    new_note = Notes(title = title,content=content,user_id=user_id) 
    db.session.add(new_note) 
    db.session.commit() 
    return new_note  

def get_note_id(note_id:int):
    note=Notes.query.get(note_id)
    return note   

def get_notes():
    notes=Notes.query.all()
    return notes     

def get_note_by_title(title:str): 
    note = Notes.query.filter_by(title=title).first() 
    return note  

def update_note(note_id,**kwargs):
    note=Notes.query.get(note_id)
    if note:
        for key,value in kwargs.items():
            setattr(note,key,value)
        db.session.commit()  
    return note  
def delete_note(note_id:int):
    notes = Notes.query.get(note_id)
    if notes:
        db.session.delete(notes) 
        db.session.commit() 
    return notes 