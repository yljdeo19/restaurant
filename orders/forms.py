from django import forms
from .models import Order, City
from django.forms import Select
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        country = forms.Select(attrs={'id': 'country', 'class': 'custom-select d-block w-100'})
        city = forms.Select(attrs={'id': 'state', 'class': 'custom-select d-block w-100'})
        widgets = {
            "first_name": forms.TextInput(
                attrs={'id': 'firstName', 'class': 'form-control'}),
            "last_name": forms.TextInput(
                attrs={'id': 'lastName', 'class': 'form-control'}),
            "email": forms.EmailInput(
                attrs={'id': 'email', 'class': 'form-control'}),
            "address": forms.TextInput(attrs={'id': 'address', 'class': 'form-control'}),
            "paid": forms.RadioSelect
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
