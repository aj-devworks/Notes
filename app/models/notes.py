from app import db 
from flask_bcrypt import check_password_hash,generate_password_hash 
from sqlalchemy.orm import Mapped,mapped_column 
from .models import User 


class Notes(db.Model):
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(nullable=False)
    content:Mapped[str]=mapped_column(nullable=False) 
    user_id:Mapped[int]=mapped_column(db.ForeignKey('user.id'),nullable=False) 

    







