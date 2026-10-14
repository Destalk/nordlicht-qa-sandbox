from datetime import datetime, timezone
from src.payments import start_payment
def test_identical_payment_retry():
    rows = {}; now = datetime(2026, 10, 1, tzinfo=timezone.utc)
    payload = {"amount_cents": 12000}
    assert start_payment("A", "key1", payload, now, rows) == start_payment("A", "key1", payload, now, rows)
