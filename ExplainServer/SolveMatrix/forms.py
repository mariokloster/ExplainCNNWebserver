from django import forms


# Create your forms here.

class Matrix(forms.Form):
    x11 = forms.FloatField()
    x21 = forms.FloatField()
    x31 = forms.FloatField()
    x12 = forms.FloatField()
    x22 = forms.FloatField()
    x32 = forms.FloatField()
    x13 = forms.FloatField()
    x23 = forms.FloatField()
    x33 = forms.FloatField()
