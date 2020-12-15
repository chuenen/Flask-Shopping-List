from project.api.models import Product, Order


class ProductBuilder:

    def __init__(self):
        self._id = 1
        self._stock_pcs = 10
        self._price = 100
        self._shop_id = 'um'
        self._vip = False
        self._orders = []

    def id(self, id_):
        self._id = id_
        return self

    def stock_pcs(self, stock_pcs):
        self._stock_pcs = stock_pcs
        return self

    def price(self, price):
        self._price = price
        return self

    def shop_id(self, shop_id):
        self._shop_id = shop_id
        return self

    def vip(self, vip):
        self._vip = vip
        return self

    def orders(self, orders):
        self._orders = orders
        return self


    def build(self):
        product = Product(
            self._stock_pcs,
            self._price,
            self._shop_id,
            self._vip
        )
        product._id = self._id
        product._orders = self._orders
        return product


class OrderBuilder:

    def __init__(self):
        self._id = 1
        self._product_id = 1
        self._customer_id = 'C001'
        self._qty = 1
        self._product = ProductBuilder().build()

    def id(self, id_):
        self._id = id_
        return self

    def customer_id(self, customer_id):
        self._customer_id = customer_id
        return self

    def qty(self, qty):
        self._qty = qty
        return self

    def product(self, product):
        self._product = product
        return self

    def build(self):
        order = Order(self._product_id, self._customer_id, self._qty)
        order._id = self._id
        order._product = self._product
        return order



# vi:et:ts=4:sw=4:cc=80
