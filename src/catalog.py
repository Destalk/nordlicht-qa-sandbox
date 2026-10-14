"""SYNTHETIC: Artikelkatalog; related Jira epic KAN-213."""
def line_total(price_cents, quantity):
    if price_cents < 0 or quantity < 1:
        raise ValueError("invalid price or quantity")
    return price_cents * quantity

def order_line(article, quantity):
    if not article["released"]:
        raise ValueError("article not released")
    return {"sku": article["sku"], "tax_class": article["tax_class"], "total_cents": line_total(article["price_cents"], quantity)}
