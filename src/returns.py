"""SYNTHETIC: Retouren und Erstattungen; related Jira epic KAN-217."""
def refund(payment, amount_cents, key):
    if key in payment["refunds"]:
        return payment["refunds"][key]
    remaining = payment["paid_cents"] - sum(payment["refunds"].values())
    if amount_cents > remaining:
        raise ValueError("refund exceeds remaining amount")
    payment["refunds"][key] = amount_cents
    return amount_cents
