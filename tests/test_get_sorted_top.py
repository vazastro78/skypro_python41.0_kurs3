from src.utils import get_sorted_top

def test_get_sorted_top():
    assert get_sorted_top([0,9,10,2,1,5], amount=2)==[10,9]
    assert get_sorted_top([0,9,10,2,1,5], amount=3)==[10,9,5]
    assert get_sorted_top([13,9,10,2,1,5], amount=4)==[13,10,9,5]
