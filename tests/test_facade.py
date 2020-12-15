from unittest.mock import patch

from .builders import ProductBuilder, OrderBuilder
from project.api import facade


@patch.object(facade, 'order_repo')
def test_get_order(repo):
    product = ProductBuilder() \
        .id(2).stock_pcs(5).price(150).shop_id('ab').vip(True).build()
    repo.get.return_value = OrderBuilder() \
        .id(10).product(product).customer_id('C002').qty(3).build()

    result = facade.get_order(10)

    repo.get.assert_called_once_with(10)
    assert result == {
        'id': 10,
        'product': {
            'id': 2,
            'stock_pcs': 5,
            'price': 150,
            'shop_id': 'ab',
            'vip': True,
        },
        'qty': 3,
        'customer_id': 'C002',
    }

@patch.object(facade, 'Order')
@patch.object(facade, 'order_repo')
def test_add_order(repo, Order):
    result = facade.add_order(1, 'C001', 5)

    Order.assert_called_once_with(1, 'C001', 5)
    repo.add.assert_called_once_with(Order.return_value)
    assert result == repo.add.return_value

@patch.object(facade, 'order_repo')
def test_remove_order(repo):
    facade.remove_order(5)

    repo.remove.assert_called_once_with(5)

@patch.object(facade, 'order_repo')
def test_list_orders(repo):
    order1 = OrderBuilder().id(1).build()
    order2 = OrderBuilder().id(2).build()
    order3 = OrderBuilder().id(3).build()
    repo.list.return_value = [order1, order2, order3]

    results = facade.list_orders()

    repo.list.assert_called_once()
    assert len(results) == 3
    assert [result['id'] for result in results] == [1, 2, 3]

@patch.object(facade, 'product_repo')
def test_get_product(repo):
    product = ProductBuilder() \
        .id(2).stock_pcs(5).price(30).shop_id('cd').vip(False).build()
    repo.get.return_value = product

    result = facade.get_product(2)

    repo.get.assert_called_once_with(2)
    assert result == {
        'id': 2,
        'stock_pcs': 5,
        'price': 30,
        'shop_id': 'cd',
        'vip': False,
    }

@patch.object(facade, 'product_repo')
def test_list_products(repo):
    product1 = ProductBuilder().id(1).build()
    product2 = ProductBuilder().id(2).build()
    product3 = ProductBuilder().id(3).build()
    repo.list.return_value = [product1, product2, product3]

    results = facade.list_products()

    repo.list.assert_called_once()
    assert len(results) == 3
    assert [result['id'] for result in results] == [1, 2, 3]

@patch.object(facade, 'product_repo')
def test_list_top3(repo):
    order1 = OrderBuilder().qty(1).build()
    order2 = OrderBuilder().qty(2).build()
    order3 = OrderBuilder().qty(3).build()
    order4 = OrderBuilder().qty(4).build()
    order5 = OrderBuilder().qty(5).build()
    product1 = ProductBuilder().id(1).orders([order1, order2]).build()
    product2 = ProductBuilder().id(2).build()
    product3 = ProductBuilder().id(3).orders([order3, order4]).build()
    product4 = ProductBuilder().id(4).orders([order5]).build()
    repo.list.return_value = [product1, product2, product3, product4]

    results = facade.list_top3()

    repo.list.assert_called_once()
    assert results == [(3, 7), (4, 5), (1, 3)]

@patch.object(facade, 'product_repo')
def test_list_shops(repo):
    order1 = OrderBuilder().qty(1).build()
    order2 = OrderBuilder().qty(2).build()
    order3 = OrderBuilder().qty(3).build()
    order4 = OrderBuilder().qty(4).build()
    order5 = OrderBuilder().qty(5).build()
    product1 = ProductBuilder().id(1).shop_id('ab').price(60).orders([order1, order2]).build()
    product2 = ProductBuilder().id(2).shop_id('cd').build()
    product3 = ProductBuilder().id(3).shop_id('ab').price(90).orders([order3, order4]).build()
    product4 = ProductBuilder().id(4).shop_id('ef').price(150).orders([order5]).build()
    repo.list.return_value = [product1, product2, product3, product4]

    results = facade.list_shops()

    repo.list.assert_called_once()
    assert results == [
        ['ab', 810, 10, 4],
        ['cd', 0, 0, 0],
        ['ef', 750, 5, 1]
    ]


# vi:et:ts=4:sw=4:cc=80
