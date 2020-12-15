from unittest.mock import patch

from project.api import main

@patch.object(main.facade, 'get_order')
def test_get_order(get_order, client):
    get_order.return_value = {'customer_id': 'C002'}

    resp = client.get('/api/orders/5')

    get_order.assert_called_once_with(5)
    assert resp.status_code == 200
    assert resp.json == {'customer_id': 'C002'}

@patch.object(main.facade, 'add_order')
def test_add_order(add_order, client):
    add_order.return_value = 3

    resp = client.post(
        '/api/orders',
        data={
            'product': 5,
            'customer_id': 'C001',
            'qty': 10
        }
    )

    add_order.assert_called_once_with(5, 'C001', 10)
    assert resp.status_code == 201
    assert resp.json == {'order_id': 3}

@patch.object(main.facade, 'remove_order')
def test_remove_order(remove_order, client):
    resp = client.delete('/api/orders/25')

    remove_order.assert_called_once_with(25)
    assert resp.status_code == 200
    assert resp.data == b'ok'

@patch.object(main.facade, 'list_orders')
def test_list_orders(list_orders, client):
    list_orders.return_value = [{'id': 3}, {'id': 7}, {'id': 8}]

    resp = client.get('/api/orders')

    list_orders.assert_called_once()
    assert resp.status_code == 200
    assert resp.json == [{'id': 3}, {'id': 7}, {'id': 8}]

@patch.object(main.facade, 'get_product')
def test_get_product(get_product, client):
    get_product.return_value = {'shop_id': 'ab'}

    resp = client.get('/api/products/9')

    get_product.assert_called_once_with(9)
    assert resp.status_code == 200
    assert resp.json == {'shop_id': 'ab'}

@patch.object(main.facade, 'list_products')
def test_list_products(list_products, client):
    list_products.return_value = [{'id': 1}, {'id': 2}]

    resp = client.get('/api/products')

    list_products.assert_called_once()
    assert resp.status_code == 200
    assert resp.json == [{'id': 1}, {'id': 2}]

@patch.object(main.facade, 'list_top3')
def test_list_top3(list_top3, client):
    list_top3.return_value = []

    resp = client.get('/api/products/top3')

    list_top3.assert_called_once()
    assert resp.status_code == 200
    assert resp.json == []

@patch.object(main.facade, 'list_shops')
def test_list_shops(list_shops, client):
    list_shops.return_value = []

    resp = client.get('/api/shops')

    list_shops.assert_called_once()
    assert resp.status_code == 200
    assert resp.json == []


# vi:et:ts=4:sw=4:cc=80
