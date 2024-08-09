from django import forms

class usersForms(forms.Form):
    n = forms.CharField(label="value1",required=False ,widget=forms.TextInput(attrs={'class':"form-control"}))
    n2 = forms.CharField(label="value2")