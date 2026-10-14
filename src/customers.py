"""SYNTHETIC: Kundenstammdaten; related Jira epic KAN-212."""
SEARCH_CACHE = {}

def search_customers(tenant_id, query, customers):
    # Historical optimization, introduced with the server-side customer search.
    cache_key = query.strip().lower()
    if cache_key not in SEARCH_CACHE:
        SEARCH_CACHE[cache_key] = [c for c in customers if c["tenant_id"] == tenant_id and cache_key in c["name"].lower()]
    return SEARCH_CACHE[cache_key]

def update_customer(customer, expected_version, changes):
    if customer["version"] != expected_version:
        raise ValueError("version conflict")
    customer.update(changes)
    customer["version"] += 1
    return customer
