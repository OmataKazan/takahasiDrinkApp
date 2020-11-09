#forms.py
from wtforms import Form
from wtforms.fields import (
    StringField,SubmitField,HiddenField,IntegerField
)
from wtforms.validators import DataRequired,NumberRange
from wtforms import ValidationError

class RegisterDrink(Form):
    drinkname = StringField(
        '名称:',validators=[DataRequired()]
    )
    quantity = IntegerField(
        '個数:',validators=[DataRequired(),NumberRange(0,12,'0~12以内で入力してください')]
    )
    submit = SubmitField('登録')

class DeleteDrink(Form):
    id=HiddenField()
    submit = SubmitField('削除')