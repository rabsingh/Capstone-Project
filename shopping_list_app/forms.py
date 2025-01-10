from django import forms
from .models import Item
from django.contrib.auth.models import User


# Form for adding or editing items
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'quantity', 'notes', 'week_beginning']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'week_beginning': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
        }


# Filtering by week_beginning, added_by , authorised
class ItemFilterForm(forms.Form):
    week_beginning = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        ),
        label='Filter by Week'
    )
    added_by = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        empty_label="All Users",
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Filter by User'
    )
    authorised = forms.ChoiceField(
        choices=[
            ('', 'All Items'),
            ('True', 'Authorized'),
            ('False', 'Not Authorized')
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Authorization Status'
    )
