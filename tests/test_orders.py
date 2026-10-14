from src.orders import create_order
def test_identical_retry():
    rows = {}; payload = {"lines": [{"sku": "A", "quantity": 1}], "delivery_address": {"city": "Demo"}}
    first = create_order("A", "key1", payload, rows)
    assert create_order("A", "key1", payload, rows) == first
    assert len(rows) == 1
