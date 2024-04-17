from src.utils import format_hide_transaction_to

def test_to():
    assert format_hide_transaction_to("Счет 90424923579946435907")=="Счет ****************5907"
