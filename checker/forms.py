from django import forms

class PasswordStrengthForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=100)

class PasswordGeneratorForm(forms.Form):
    length = forms.IntegerField(
        min_value=4, max_value=128, initial=12, 
        widget=forms.HiddenInput(attrs={'class': 'form-control', 'id': 'id_length'})
    )
    include_numbers = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    include_special = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
