from src.integrations import deliver
def test_single_delivery():
    sent = []; outbox = {}
    assert deliver({"id": "e1", "recipient": "demo@invalid.example", "message": "Order confirmed"}, lambda to, body: sent.append(to), outbox) == "delivered"
    assert len(sent) == 1
