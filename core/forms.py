from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction

        fields = [
            'name',
            'description',
            'type',
            'category',
            'amount'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter transaction name'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description',
                'rows': 3
            }),

            'type': forms.Select(attrs={
                'class': 'form-select'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select'
            }),

            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter amount'
            }),
        }