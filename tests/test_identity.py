from datetime import datetime, timezone
from src.identity import accept_invitation
def test_first_invitation():
    now = datetime(2026, 10, 1, tzinfo=timezone.utc)
    row = {"issued_at": now, "used": False, "email": "Demo@invalid.example", "tenant_id": "A"}
    assert accept_invitation(row, now)["email"] == "demo@invalid.example"
