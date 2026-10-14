"""SYNTHETIC: Versand; related Jira epic KAN-218."""
def label_for(order, customer):
    if order["payment_status"] != "paid":
        raise ValueError("payment not confirmed")
    return {"order_id": order["id"], "address": dict(customer["delivery_address"])}
