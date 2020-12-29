#forms.py
from wtforms import Form
from wtforms.fields import (
    StringField,SubmitField,HiddenField,IntegerField,PasswordField
)
from wtforms.validators import DataRequired,NumberRange,EqualTo
from wtforms import ValidationError

#-----ログイン・登録管理フォーム----#
class LoginForm(Form):
    username = StringField(
        'ユーザ名',validators=[DataRequired()]
    )
    password = PasswordField(
        'パスワード',validators=[DataRequired()]
    )
    submit = SubmitField('ログイン')

class RegisterForm(Form):
    username = StringField(
        'ユーザ名',validators=[DataRequired()]
    )
    password = PasswordField(
        'パスワード',validators=[DataRequired(),EqualTo('confirm_password',message='パスワードが一致しません。もう一度確認してください')]
    )
    confirm_password = PasswordField(
        'パスワード確認',validators=[DataRequired()]
    )
    submit = SubmitField('登録')

    #ユーザ名がすでに登録されている場合のエラー
    def validate_username(self, field):
        if User.select_by_username(field.data):
            raise ValidationError('そのユーザ名は使われています')
#-----ログイン・ログアウト管理フォーム----#

#-----ドリンクの管理フォーム----#
class RegisterDrink(Form):
    drinkname = StringField(
        '名称:',validators=[DataRequired()]
    )
    quantity = IntegerField(
        '個数:',validators=[DataRequired(),NumberRange(0,25,'0~24以内で入力してください')]
    )
    submit = SubmitField('追加する')

class DeleteDrink(Form):
    id=HiddenField()
    submit = SubmitField('削除')
#-----ドリンクの管理フォーム-----#