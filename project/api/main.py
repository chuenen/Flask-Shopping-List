from flask import Blueprint, request, jsonify

from . import facade
from .repos import order_repo, product_repo
from .models import Order


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    data = facade.get_order(order_id)
    return jsonify(data)

@api.route('/orders', methods=['POST'])
def add_order():
    form = request.form
    product_id = int(form['product'])
    customer_id = form['customer_id']
    qty = int(form['qty'])

    order_id = facade.add_order(product_id, customer_id, qty)
    return jsonify({'order_id': order_id}), 201

@api.route('/orders/<int:order_id>', methods=['DELETE'])
def remove_order(order_id):
    facade.remove_order(order_id)
    return 'ok', 200

@api.route('/orders', methods=['GET'])
def list_orders():
    orders = facade.list_orders()
    return jsonify(orders)

@api.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    data = facade.get_product(product_id)
    return jsonify(data)

@api.route('/products', methods=['GET'])
def list_products():
    products = facade.list_products()
    return jsonify(products)

@api.route('/products/top3', methods=['GET'])
def list_top3():
    top3 = facade.list_top3()
    return jsonify(top3)

@api.route('/shops', methods=['GET'])
def list_shops():
    shops = facade.list_shops()
    return jsonify(shops)


# vi:et:ts=4:sw=4:cc=80
