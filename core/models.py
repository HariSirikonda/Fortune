import uuid
from django.db import models

# Create your models here.
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    TRANSACTION_TYPES = [
        ("income", "Income"),
        ("expense", "Expense"),
    ]
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    CATEGORIES = [
        ("salary", "Salary"),
        ("food", "Food"),
        ("groceries", "Groceries"),
        ("rent", "Rent"),
        ("utilities", "Utilities"),
        ("transport", "Transport"),
        ("fuel", "Fuel"),
        ("shopping", "Shopping"),
        ("entertainment", "Entertainment"),
        ("healthcare", "Healthcare"),
        ("education", "Education"),
        ("travel", "Travel"),
        ("insurance", "Insurance"),
        ("investments", "Investments"),
        ("bills", "Bills"),
        ("subscriptions", "Subscriptions"),
        ("personal_care", "Personal Care"),
        ("gifts", "Gifts"),
        ("other", "Other"),
    ]
    category = models.CharField(max_length=20, choices=CATEGORIES)
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