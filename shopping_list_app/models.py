from django.db import models
from django.contrib.auth.models import User  # Import Django's built-in User model

# Items Table
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True, null=True)
    authorised = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="added_items")
    week_beginning = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} ({'Authorised' if self.authorised else 'Pending'})"
