from src.reporting import financial_totals
def test_net_amount():
    assert financial_totals(10000, [3000])["net"] == 7000
