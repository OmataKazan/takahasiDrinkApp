#models.py
from flaskr import db,ma
from datetime import datetime
#-------ユーザ情報テーブル-------

#-------ユーザ情報テーブル-------
#-------ドリンク情報を保管するテーブル-------
class DrinkList(db.Model):
    __tablename__ = 'drinkList'
    id = db.Column(db.Integer,primary_key=True)
    productName = db.Column(db.String(64),index=True)
    jancode = db.Column(db.String(64))
    create_at=db.Column(db.DateTime,default=datetime.now)

    def __init__(self,productName,jancode):
        self.productName=productName
        self.jancode=jancode

class DrinkSchema(ma.Schema):
    class Meta:
        fields = ("drink_id","productName","jancode","create_at")
#-------ドリンク情報を保管するテーブル-------
drink_schema = DrinkSchema()