from src.inventory import reserve_order
def test_single_reservation():
    stock = {"A": {"physical": 2, "reserved": 0}}
    assert reserve_order(stock, [{"sku": "A", "quantity": 1}])[0]["quantity"] == 1
