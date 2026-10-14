"""SYNTHETIC: Identität und Rollen; related Jira epic KAN-8."""
from datetime import timedelta

def accept_invitation(invitation, now):
    if invitation["used"] or now >= invitation["issued_at"] + timedelta(hours=24):
        raise ValueError("invitation unavailable")
    invitation["used"] = True
    return {"email": invitation["email"].lower(), "tenant_id": invitation["tenant_id"]}
