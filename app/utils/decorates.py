from functools import wraps 
from flask import jsonify 
from flask_jwt_extended import get_jwt_identity 




def owner_required(resource_func):
    def decorater(f):
        @wraps(f) 
        def wrappers(resource_id,*args,**kwargs): 
            resource = resource_func(resource_id)  
            if resource.user_id != get_jwt_identity():
                return ('forbidden') 
            return f(resource_id,*args,**kwargs) 

