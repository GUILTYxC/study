from django import forms

class CardActivationForm(forms.Form):
    code = forms.CharField(label='卡密', max_length=20)
