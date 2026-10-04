from app.repository import create_note,get_note_id,get_notes,get_note_by_title,update_note,delete_note  



def create_note_service(title:str,content:str,user_id:int):  
    if not title or not content:
        raise ValueError("all fields are required") 
    note=create_note(title,content,user_id) 
    return note   
def get_note_service(id:int):
    notes=get_note_id(id) 
    if not notes:
        raise ValueError("note not found") 
    return notes 
def get_notes_services():
    notes=get_notes()
    return notes  
def get_note_by_title_service(title:str): 
    note=get_note_by_title(title) 
    if not note:
        raise ValueError("note not found") 
    return note
def update_note_service(note_id:int,**kwargs):
    note=update_note(note_id,**kwargs) 
    if not note:
        raise ValueError("note not found") 
    return note
def delete_note_service(note_id:int):
    note=delete_note(note_id) 
    if not note:
        raise ValueError("note not found") 
    return note  