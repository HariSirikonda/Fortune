import uuid
from django.db import models

# Create your models here.
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    types = {"income": "Income", "expense" : "Expense", "savings": "Savings", "returns": "Returns"}
    type = models.CharField(max_length=10, choices=types)
    categories = {
    "housing": "Housing",
    "utilities": "Utilities",
    "transportation": "Transportation",
    "groceries": "Groceries",
    "healthcare": "Healthcare",
    "insurance": "Insurance",
    "dining_out": "Dining Out",
    "entertainment": "Entertainment",
    "subscriptions": "Subscriptions",
    "shopping": "Shopping",
    "travel": "Travel",
    "personal_care": "Personal Care",
    "debt_payment": "Debt Payment"
    }
    category = models.CharField(max_length=20, choices=categories)
    month_code = models.CharField(max_length=7, editable=False)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.month_code = self.created_at.strftime("%b%Y").upper()
        super().save(update_fields=["month_code"])