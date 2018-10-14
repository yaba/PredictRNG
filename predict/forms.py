from django import forms


class InputForm(forms.Form):
    post = forms.CharField(widget=forms.Textarea)
