#models.py
from flaskr import db
from datetime import datetime

class DrinkList(db.Model):
    __tablename__ = 'drinkList'
    id = db.Column(db.Integer,primary_key=True)
    productName = db.Column(db.String(64),index=True)
    jancode = db.Column(db.String(64))
    create_at=db.Column(db.DateTime,default=datetime.now)

    def __init__(self,productName,jancode):
        self.productName=productName
        self.jancode=jancode