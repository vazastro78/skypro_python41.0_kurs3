from src.utils import get_executed_transactions


json_data=[
{'date':'2019-10-01','state':'EXECUTED'},
{'date':'2010-01-01','state':'CANCELED'}
]

def test_get_executed_transactions():
    assert get_executed_transactions(json_data)=={ '2019-10-01': {'date':'2019-10-01','state':'EXECUTED'} }
