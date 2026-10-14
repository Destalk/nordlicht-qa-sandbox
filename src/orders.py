"""SYNTHETIC: Aufträge und Checkout; related Jira epic KAN-215."""
def create_order(tenant_id, key, payload, orders):
    identity = (tenant_id, key)
    if identity in orders:
        return orders[identity]
    order = {"id": "order-" + str(len(orders) + 1), "tenant_id": tenant_id, "lines": payload["lines"], "delivery_address": dict(payload["delivery_address"])}
    orders[identity] = order
    return order
