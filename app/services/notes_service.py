from .repository import create_note, get_notes_id, update_note, delete_note
from .repository import create_user, get_user_by_username, get_user_by_id, get_all_users, update_user


def create_note_service(title, content, user_id):
    if not title or not content:
        raise ValueError("Title and content are required fields")
    return create_note(title, content, user_id)


def get_note_service(notes_id):
    if not notes_id:
        raise ValueError("Note id is required")
    note = get_notes_id(notes_id)
    if not note:
        raise ValueError("Note not found")
    return note


def update_note_service(notes_id, **kwargs):
    if not notes_id:
        raise ValueError("Note id is required")
    return update_note(notes_id, **kwargs)


def delete_note_service(notes_id):
    if not notes_id:
        raise ValueError("Note id is required")
    return delete_note(notes_id) 