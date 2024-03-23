from django import forms
from .models import FoodOrder

class FoodOrderForm(forms.ModelForm):
    class Meta:
        model = FoodOrder
        fields = '__all__'

        widgets = {
            'person_name': forms.TextInput(attrs={'class':'form-control'}),
            'order': forms.Select(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'time_of_order': forms.DateTimeInput(attrs={'type':'date','class':'form-control'}),
            'delivered': forms.NullBooleanSelect(attrs={'class':'form-control'})
        }