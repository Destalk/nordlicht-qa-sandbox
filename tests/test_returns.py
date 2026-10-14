from src.returns import refund
def test_valid_partial_refund():
    payment = {"paid_cents": 10000, "refunds": {}}
    assert refund(payment, 3000, "r1") == 3000
