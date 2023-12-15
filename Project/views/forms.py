from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, IntegerField, FloatField, URLField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class ItemForm(FlaskForm):
    id = HiddenField("id", validators=[Optional()])
    name = StringField("name", validators=[DataRequired(), Length(max=300)])
    description = TextAreaField("description", validators=[DataRequired()])
    stock = IntegerField("stock", validators=[NumberRange(min=0)])
    unit_price = FloatField("unit_price", validators=[NumberRange(min=0)])
    image = URLField("image", validators=[Optional()])
    submit = SubmitField("Save")

class ProductFetchForm(FlaskForm):
    limit = IntegerField("Limit", default=1)
    submit = SubmitField("Fetch")