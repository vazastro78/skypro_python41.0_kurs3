from src.utils import construct_transaction

item={
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
    }

def test_construct_transaction():
    assert construct_transaction(item)=={
            'date_formated': '04.04.2019',
            'description': 'Перевод со счета на счет',
            'from_hide': 'Счет 1970 86** **** **** 8542',
            'sum': '79114.93 USD',
            'to_hide': 'Счет ****************4188'
             }
