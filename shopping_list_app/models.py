from django.db import models 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime

def validate_monday(value):
    if value.weekday() != 0:
        raise ValidationError('Week beginning date must be a Monday.')

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True, null=True)
    authorised = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="added_items")
    week_beginning = models.DateField(validators=[validate_monday])
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.item_name} ({'Authorised' if self.authorised else 'Pending'})"