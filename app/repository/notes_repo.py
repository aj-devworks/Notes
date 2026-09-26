from SQLAlchemyError import sqlalchemy_error  
from models import Notes 



def create_note(title,content,created_at,updated_at):   
    new_note=Notes(title=title,content=content,createed_at=created_at,updated_at=updated_at) 
    try:
        new_note.commit()
        return new_note 
    except sqlalchemy_error as e:
        print(f"Error creating note:{e}")     

def get_notes_id(notes_id):
    try:
        note=Notes.query.get(notes_id) 
        return note 
    excep sqlalchemy_error as e:
    print(f"the passed note id is not found:{e}") 
          
