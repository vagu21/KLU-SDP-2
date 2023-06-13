from django import forms


from .models import Customer


class Customer(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

# class Book(forms.ModelForm):
#     class Meta:
#         model=Book
#         fields="__all__"