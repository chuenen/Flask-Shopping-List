from functools import wraps

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
)

from .. import config
from ..utils import http_post, http_get, http_delete
from .forms import OrderForm


web = Blueprint(
    'web',
    __name__,
    static_folder='../static',
    template_folder='../templates'
)


def identity_and_inventory_checked(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        form=request.form

        vip = bool(form.get('vip'))
        product_id = form['product']
        product = http_get(f'{config.host}/api/products/{product_id}').json()

        vip_mismatch = vip != product['vip'] if product['vip'] else False
        understock = product['stock_pcs'] == 0

        if vip_mismatch or understock:
            return redirect(url_for(
                '.index',
                product_id=product_id,
                vip_mismatch=vip_mismatch,
                understock=understock,
            ))

        return func(*args, **kwargs)
    return wrapper

def new_arrived(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        order_id = kwargs['order_id']
        order = http_get(f'{config.host}/api/orders/{order_id}').json()
        if order['product']['stock_pcs'] == 0:
            func(*args, **kwargs)
            return redirect(url_for(
                '.index',
                product_id=order['product']['id'],
                new_arrived=True,
            ))

        return func(*args, **kwargs)
    return wrapper

@web.route('/products', methods=['GET', 'POST'])
def index():
    product_id = request.args.get('product_id')
    vip_mismatch = request.args.get('vip_mismatch') == 'True'
    understock = request.args.get('understock') == 'True'
    new_arrived = request.args.get('new_arrived') == 'True'

    form = OrderForm()
    return render_template(
        'index.html',
        form=form,
        products=get_products(),
        orders=get_orders(),
        top3=get_top3(),
        product_id=product_id,
        vip_mismatch=vip_mismatch,
        understock=understock,
        new_arrived=new_arrived,
    )

@web.route('/add_order', methods=['POST'])
@identity_and_inventory_checked
def add_order():
    http_post(f'{config.host}/api/orders', data=request.form)
    return redirect(url_for('.index'))

@web.route('/remove_order/<int:order_id>', methods=['POST'])
@new_arrived
def remove_order(order_id):
    http_delete(f'{config.host}/api/orders/{order_id}')
    return redirect(url_for('.index'))

def get_top3():
    return http_get(f'{config.host}/api/products/top3').json()

def get_products():
    return http_get(f'{config.host}/api/products').json()

def get_orders():
    return http_get(f'{config.host}/api/orders').json()


# vi:et:ts=4:sw=4:cc=80
