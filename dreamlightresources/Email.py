from django import forms
class email(forms.Form):
    Email = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;'}))