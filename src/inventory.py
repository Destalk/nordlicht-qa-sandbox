"""SYNTHETIC: Bestand und Reservierung; related Jira epic KAN-214."""
def reserve(stock, sku, quantity):
    available = stock[sku]["physical"] - stock[sku]["reserved"]
    if available < quantity:
        raise ValueError("insufficient stock")
    stock[sku]["reserved"] += quantity
    return {"sku": sku, "quantity": quantity}

def reserve_order(stock, lines):
    return [reserve(stock, line["sku"], line["quantity"]) for line in lines]
