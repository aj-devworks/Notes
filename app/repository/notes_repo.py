from extensions import db
from models import Notes

def create_note(title, content, user_id):
    new_note = Notes(title=title, content=content, user_id=user_id)
    db.session.add(new_note)
    db.session.commit()
    return new_note

def get_notes_id(notes_id):
    return Notes.query.get(notes_id)

def get_all_notes():
    return Notes.query.all()

def update_note(notes_id, **kwargs):
    note = Notes.query.get(notes_id)
    if not note:
        raise ValueError("Note not found")
    for key, value in kwargs.items():
        setattr(note, key, value)
    db.session.commit()
    return note

def delete_note(notes_id):
    note = Notes.query.get(notes_id)
    if not note:
        raise ValueError("Note not found")
    db.session.delete(note)
    db.session.commit()
    return note