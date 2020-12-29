#models.py
from flaskr import db,ma
from datetime import datetime
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash,check_password_hash

#-------ユーザ情報テーブル-------#
class User(UserMixin,db.Model):
    #テーブル定義
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True,nullable=False)
    password = db.Column(db.String(64),nullable=False)
    create_at=db.Column(db.DateTime,default=datetime.now)
    update_at=db.Column(db.DateTime,default=datetime.now)

    #初期化
    def __init__(self,username,password):
        self.username = username
        self.password = generate_password_hash(password)

    #入力されたパスワードが登録されたパスワードと一致しているか
    def validate_password(self,password):
        return check_password_hash(self.password,password)

    #ユーザ追加
    def add_user(self):
        with db.session.begin(subtransactions=True):
            db.session.add(self)
        db.session.commit()

    #usernameからレコードの取り出し
    @classmethod
    def select_by_username(cls,username):
        return cls.query.filter_by(username=username).first()
#-------ユーザ情報テーブル-------#

#-------ドリンク情報を保管するテーブル-------#
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
#-------ドリンク情報を保管するテーブル-------#

drink_schema = DrinkSchema()