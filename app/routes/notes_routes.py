from app.services.notes_service import create_note_service, get_note_service, get_all_notes_service, update_note_service, delete_note_service
from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

note_bp = Blueprint("notes", __name__)


@note_bp.route("/notes", methods=['POST'])
@jwt_required()
def create_note():
    user_id = get_jwt_identity()
    data = request.get_json(silent=True) or {}
    title = data.get('title')
    content = data.get('content')
    try:
        note = create_note_service(title, content, user_id)
        return jsonify({"id": note.id, "title": note.title, "content": note.content, "user_id": note.user_id}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@note_bp.route('/notes/<int:note_id>', methods=['GET'])
@jwt_required()
def get_note(note_id):
    try:
        note = get_note_service(note_id)
        return jsonify({"id": note.id, "title": note.title, "content": note.content, "user_id": note.user_id}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@note_bp.route("/notes", methods=['GET'])
@jwt_required()
def get_notes_all():
    notes = get_all_notes_service()
    return jsonify([
        {"id": note.id, "title": note.title, "content": note.content, "user_id": note.user_id}
        for note in notes
    ]), 200


@note_bp.route("/notes/<int:note_id>", methods=['DELETE'])
@jwt_required()
def delete_note(note_id):
    try:
        note = delete_note_service(note_id)
        return jsonify({"message": "note successfully deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400