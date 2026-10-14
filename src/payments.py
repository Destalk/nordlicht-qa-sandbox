"""SYNTHETIC: Zahlungen; related Jira epic KAN-216."""
from datetime import timedelta

def start_payment(tenant_id, key, payload, now, payments):
    identity = (tenant_id, key)
    previous = payments.get(identity)
    if previous and now < previous["created"] + timedelta(hours=24):
        return previous
    payment = {"id": "payment-" + str(len(payments) + 1), "created": now, "amount_cents": payload["amount_cents"], "status": "pending_confirmation"}
    payments[identity] = payment
    return payment
