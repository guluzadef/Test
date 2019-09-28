from django import forms
from .models import Meals
class AddFood(forms.ModelForm):
    class Meta:
        model=Meals
        fields = ["name", "category", "gram_one_porsion","ingredients","aditional_info","delivery_type","price","quantity"]
        # widgets = {
        #     "name": forms.TextInput(attrs={
        #         "class": "form-control"
        #     }),
        #     "category": forms.Select(attrs={
        #         "class": "form-control"
        #     }),
        #     "gram_one_porsion": forms.IntegerField(attrs={
        #         "class": "form-control"
        #     }),
        #     "ingredients": forms.Textarea(attrs={
        #         "class": "form-control"
        #     }),
        #     "aditional_info": forms.Textarea(attrs={
        #         "class": "form-control"
        #     }),
        #     "delivery_type": forms.Select(attrs={
        #         "class": "form-control"
        #     }),
        #     "price": forms.IntegerField(attrs={
        #         "class": "form-control"
        #     }),
        #
        #     "quantity": forms.IntegerField(attrs={
        #         "class": "form-control"
        #     }),
        #
        # }