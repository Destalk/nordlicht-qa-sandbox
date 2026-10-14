from src.customers import search_customers, SEARCH_CACHE
def test_search_same_tenant():
    SEARCH_CACHE.clear()
    assert len(search_customers("A", "Nordlicht", [{"tenant_id": "A", "name": "Nordlicht Handel"}])) == 1
