from src.utils import format_date

def test_format_date():
    assert format_date("2019-12-08T22:46:21.935582")=="08.12.2019"
    assert format_date("2009-02-07T06:17:14.634890")=="07.02.2009"

