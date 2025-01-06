from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'quantity', 'notes', 'week_beginning']
        widgets = {
            'week_beginning': forms.DateInput(attrs={'type': 'date'})
        }