import enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Enum, ForeignKey


Base = declarative_base()


class VIP(enum.Enum):
    false = 0
    true = 1


class Disabled(enum.Enum):
    false = 0
    true = 1


class Product(Base):
    __tablename__ = 'product'
    _id = Column('id', Integer, primary_key=True)
    _stock_pcs = Column('stock_pcs', Integer)
    _price = Column('price', Integer)
    _shop_id = Column('shop_id', String)
    _vip = Column('vip', Enum(VIP))
    _disabled = Column('disabled', Enum(Disabled))

    _orders = relationship('Order', backref='product')

    def __init__(self, stock_pcs, price ,shop_id, vip):
        self._stock_pcs = stock_pcs
        self._price = price
        self._shop_id = shop_id
        self._vip = VIP.true if vip else VIP.false
        self._disabled = Disabled.false

    @property
    def id(self):
        return self._id

    @property
    def stock_pcs(self):
        qty = 0
        if self.orders:
            qty = sum(order.qty for order in self.orders)
        return self._stock_pcs - qty

    @property
    def price(self):
        return self._price

    @property
    def shop_id(self):
        return self._shop_id

    @property
    def vip(self):
        return self._vip == VIP.true

    @property
    def orders(self):
        return [order for order in self._orders if order.disabled != Disabled.true]

    @hybrid_property
    def disabled(self):
        return self._disabled

    def to_dict(self):
        return {
            'id': self._id,
            'stock_pcs': self.stock_pcs,
            'price': self._price,
            'shop_id': self._shop_id,
            'vip': self.vip,
        }


class Order(Base):
    __tablename__ = 'order'
    _id = Column('id', Integer, primary_key=True)
    _product_id = Column('product_id', Integer, ForeignKey('product.id'))
    _customer_id = Column('customer_id', Integer)
    _qty = Column('qty', Integer)
    _disabled = Column('disabled', Enum(Disabled))

    _product = relationship('Product')

    def __init__(self, product_id, customer_id, qty):
        self._product_id = product_id
        self._customer_id = customer_id
        self._qty = qty
        self._disabled = Disabled.false

    @hybrid_property
    def id(self):
        return self._id

    @property
    def qty(self):
        return self._qty

    @property
    def product(self):
        return self._product

    @hybrid_property
    def disabled(self):
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        self._disabled = disabled

    def to_dict(self):
        return {
            'id': self._id,
            'product': self._product.to_dict(),
            'qty': self.qty,
            'customer_id': self._customer_id,
        }


# vi:et:ts=4:sw=4:cc=80
