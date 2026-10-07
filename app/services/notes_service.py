from app.reposirtory import create_note_repo 



def create_note_service(title, content, user_id):
if not title or not content:
    raise ValueError("all fields are required") 
return create_note_repo(title, content, user_id)  
