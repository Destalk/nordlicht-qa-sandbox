"""SYNTHETIC: Integrationen und Benachrichtigungen; related Jira epic KAN-220."""
def deliver(event, send, outbox):
    send(event["recipient"], event["message"])
    outbox[event["id"]] = "delivered"
    return "delivered"
