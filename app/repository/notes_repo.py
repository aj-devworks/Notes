from app.model import Notes  




def create_note_repo(title,content,user_id): 
    nw_note =Notes(title=title,content=content,user_id=user_id) 
    db.session.add(nw_note) 
    db.session.commit()  
    return nw_note  


