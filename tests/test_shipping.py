from src.shipping import label_for
def test_paid_order_label():
    order = {"id": "A-100", "payment_status": "paid", "delivery_address": {"city": "Demo"}}
    assert label_for(order, {"delivery_address": {"city": "Demo"}})["address"]["city"] == "Demo"
