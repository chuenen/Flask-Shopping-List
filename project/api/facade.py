from .db import transaction
from .models import Order
from .repos import order_repo, product_repo


@transaction()
def get_order(order_id):
    return order_repo.get(order_id).to_dict()

@transaction()
def add_order(product_id, customer_id, qty):
    order = Order(product_id, customer_id, qty)
    return order_repo.add(order)

@transaction()
def remove_order(order_id):
    order_repo.remove(order_id)

@transaction()
def list_orders():
    return [order.to_dict() for order in order_repo.list()]

@transaction()
def get_product(product_id):
    return product_repo.get(product_id).to_dict()

@transaction()
def list_products():
    return [product.to_dict() for product in product_repo.list()]

@transaction()
def list_top3():
    sales = []
    for product in product_repo.list():
        total = sum(map(lambda x: x.qty, product.orders))
        if total > 0:
            sales.append((product.id, total))
    return sorted(sales, key=lambda x: x[1], reverse=True)[:3]


# vi:et:ts=4:sw=4:cc=80
