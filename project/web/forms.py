from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField


class OrderForm(FlaskForm):
    qty = StringField('數量')
    customer_id = StringField('Customer ID')
    product = SelectField('Product')
    vip = BooleanField('VIP 身份')


# vi:et:ts=4:sw=4:cc=80
