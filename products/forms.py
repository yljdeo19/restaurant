from django import forms
from string import Template
from products.models import Product, Category
from django.forms import ImageField
from django.forms import Select


class Select(Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        if not option.get('value'):
            option['attrs']['disabled'] = 'disabled'

        if option.get('value') == 2:
            option['attrs']['disabled'] = 'disabled'

        return option


class products(forms.ModelForm):
    category = forms.Select(attrs={'class': 'form-control mb-4'})
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control mb-4', 'id': 'acc'}))

    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'image', 'price', 'is_active')
        widgets = {
            "name": forms.TextInput(
                attrs={'placeholder': 'Title', 'id': 'defaultContactFormName', 'class': 'form-control mb-4'}),
            "description": forms.Textarea(
                attrs={'placeholder': 'Description', 'id': 'exampleFormControlTextarea5', 'class': 'form-control',
                       'rows': '3'}),
            "price": forms.NumberInput(attrs={'class': 'form-control mb-4'}),

        }
