"""SYNTHETIC: Auswertungen und Audit; related Jira epic KAN-219."""
import csv
from io import StringIO

def export_customers(customers):
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["customer_number", "name"])
    writer.writerows((c["customer_number"], c["name"]) for c in customers)
    return output.getvalue()

def financial_totals(paid_cents, refunds):
    refunded = sum(refunds)
    return {"gross": paid_cents, "refunds": refunded, "net": paid_cents - refunded}
