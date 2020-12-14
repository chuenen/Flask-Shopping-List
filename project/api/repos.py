from .db import get_session
from .models import Product, Order, Disabled


class BaseRepository:

    MODEL_CLS = None

    @property
    def _session(self):
        return get_session()

    def get(self, id_):
        return self._session.query(self.MODEL_CLS).filter_by(_id=id_).one()

    def list(self):
        return self._session.query(self.MODEL_CLS).filter_by(
            disabled=Disabled.false).all()


class ProductRepository(BaseRepository):

    MODEL_CLS = Product


class OrderRepository(BaseRepository):

    MODEL_CLS = Order

    def add(self, entity):
        self._session.add(entity)
        self._session.flush()
        return entity.id

    def remove(self, id_):
        order = self.get(id_)
        order._disabled = Disabled.true


product_repo = ProductRepository()
order_repo = OrderRepository()


# vi:et:ts=4:sw=4:cc=80
