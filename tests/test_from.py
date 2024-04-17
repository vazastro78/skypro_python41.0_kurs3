from src.utils import format_hide_transaction_from

def test_from():
    assert format_hide_transaction_from("Visa Classic 2842878893689012")=="Visa Classic 2842 87** **** 9012"
    assert format_hide_transaction_from("Maestro 7810846596785568")=="Maestro 7810 84** **** 5568"

