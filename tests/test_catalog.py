from src.catalog import line_total
def test_cent_arithmetic():
    assert line_total(10, 3) == 30
