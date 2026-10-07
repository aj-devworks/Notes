from marshmallow import schema,fields,validate 


class NotesSchema(schema):
    id = fields.int(dump=True) 
    title=fields.str(required=True,validate=validate.Length(min=1,max=100)) 
    content = fields.str(required=True,validate=validate.Length(min=1,max=250)) 
    user_id=fields.int(dump_only=True) 





note=NotesSchema()
notes=NotesSchema(many=True)  
