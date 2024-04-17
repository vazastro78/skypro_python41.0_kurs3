from src.utils import load_operations

def test_load_operations():
    assert load_operations(filename="operations.json",datadir="../data")[0]["date"]=="2019-08-26T10:50:58.294041"
    assert load_operations(filename="operations.json",datadir="../data")[1]["from"]=="MasterCard 7158300734726758"


