from app import db 
from bcrypt import check_password_hash,generate_password_hash 
from sqlalchemy.orm import Mapped,mapped_column 




class User(db.Model):
    id:Mapped[int]=mapped_column(primary_key=True)
    user_name:Mapped[str]=mapped_column(nullable=False,unique=True) 
    email:Mapped[str]=mapped_column(unique=True,nullable=False)
    password_hash:Mapped[str]=mapped_column(nullable=False) 


    notes=db.relationship('Notes',backref='user',lazy=True)



    def set_password(self,password):
        self.password_hash=generate_password_hash(password) 

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)  