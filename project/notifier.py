from prettytable import PrettyTable

from . import config
from .utils import post_message, http_get


def main():
    shops = http_get(f'{config.host}/api/shops').json()

    table = PrettyTable()
    table.field_names = ['shop_id', 'total_revenue', 'total_amount', 'total_orders']
    table.add_rows(shops)

    post_message(config.slack_webhook, f'```{table}```')


# vi:et:ts=4:sw=4:cc=80
