from dataclasses import fields
from django import forms
from .models import Pizza,Size

# class PizzaForm(forms.Form):
#     topping1=forms.MultipleChoiceField(choices=[('olives','Olives'),('pep','pepproni')],widget=forms.CheckboxSelectMultiple)
#     topping2=forms.CharField(label='Topping 2',max_length=100,widget=forms.Textarea)
#     size=forms.ChoiceField(label='Size',choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])




class PizzaForm(forms.ModelForm):
    size=forms.ModelChoiceField(queryset=Size.objects, empty_label=None,widget=forms.RadioSelect,)
    class Meta:
        model=Pizza
        fields=['topping1',"topping2",'size']
        labels={
            'topping1':'Topping 1'
        }
        widgets={'topping1':forms.Textarea}