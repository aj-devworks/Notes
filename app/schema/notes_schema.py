from marshmallow import validate,fields,Schema  






class NotesSchema(Schema):
    id =fields.Int (dump_only=True) 
    title=fields.Str(required=True,validate=validate.length(min=1,max=100))
    content=fields.Str(required=True,validate=validate.length(min=1,max=100))
    user_id =fields.Int (dump_only=True) 



note_schema = NotesSchema() 
notes_list_schema = NotesSchema(many=True)


