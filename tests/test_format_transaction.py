from src.utils import format_transaction

def test_format_transaction():
    item = {'date_formated': '08.12.2019', 'from_hide': 'неизвестный отправитель', 'to_hide': 'Счет ****************5907', 'description': 'Открытие вклада', 'sum': '41096.24 USD'}
    assert format_transaction(item)=="""
08.12.2019 Открытие вклада
неизвестный отправитель -> Счет ****************5907
41096.24 USD

"""
